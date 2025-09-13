# Gen-Z Java Streams Mini Handbook ☕
*Modern Streaming for Java Developers*

**Author:** Mohammad S Hossain

---

## Table of Contents

1. [Java Streams API](#java-streams-api)
2. [Reactive Streams](#reactive-streams)
3. [Kafka Integration](#kafka-integration)
4. [WebFlux Streaming](#webflux-streaming)
5. [Performance Tips](#performance-tips)
6. [Common Patterns](#common-patterns)
7. [Testing Streams](#testing-streams)
8. [Best Practices](#best-practices)
9. [Quick Reference](#quick-reference)

---

## Java Streams API

### Stream Creation

```java
// From collections
List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
Stream<String> stream = names.stream();

// From arrays
String[] array = {"a", "b", "c"};
Stream<String> streamFromArray = Arrays.stream(array);

// Generate streams
Stream<Integer> infiniteStream = Stream.iterate(0, n -> n + 1);
Stream<Double> randomStream = Stream.generate(Math::random);

// Range streams
IntStream range = IntStream.range(1, 10); // 1 to 9
IntStream rangeClosed = IntStream.rangeClosed(1, 10); // 1 to 10
```

### Essential Operations

```java
List<Person> people = getPeople();

// Filter, map, collect
List<String> adultNames = people.stream()
    .filter(p -> p.getAge() >= 18)
    .map(Person::getName)
    .map(String::toUpperCase)
    .collect(Collectors.toList());

// Group by
Map<String, List<Person>> peopleByCity = people.stream()
    .collect(Collectors.groupingBy(Person::getCity));

// Partition
Map<Boolean, List<Person>> adultPartition = people.stream()
    .collect(Collectors.partitioningBy(p -> p.getAge() >= 18));

// Reduce operations
OptionalInt maxAge = people.stream()
    .mapToInt(Person::getAge)
    .max();

double averageAge = people.stream()
    .mapToInt(Person::getAge)
    .average()
    .orElse(0.0);
```

### Parallel Streams

```java
// Automatic parallelization
List<String> results = largeDataSet.parallelStream()
    .filter(this::expensiveOperation)
    .map(this::transform)
    .collect(Collectors.toList());

// Custom thread pool
ForkJoinPool customThreadPool = new ForkJoinPool(4);
try {
    List<String> results = customThreadPool.submit(() ->
        largeDataSet.parallelStream()
            .map(this::process)
            .collect(Collectors.toList())
    ).get();
} finally {
    customThreadPool.shutdown();
}
```

---

## Reactive Streams

### Project Reactor (WebFlux)

```java
// Flux - 0 to N elements
Flux<String> flux = Flux.just("a", "b", "c")
    .map(String::toUpperCase)
    .filter(s -> s.length() > 0);

// Mono - 0 to 1 element  
Mono<String> mono = Mono.just("hello")
    .map(String::toUpperCase)
    .defaultIfEmpty("DEFAULT");

// Create from publisher
Flux<Long> interval = Flux.interval(Duration.ofSeconds(1))
    .take(10);

// Error handling
Flux<String> withErrorHandling = Flux.just("a", "b", "error", "d")
    .map(s -> {
        if ("error".equals(s)) {
            throw new RuntimeException("Error occurred");
        }
        return s.toUpperCase();
    })
    .onErrorReturn("FALLBACK")
    .onErrorResume(throwable -> Flux.just("RECOVERED"));
```

### Backpressure Handling

```java
Flux<Integer> source = Flux.range(1, 1000);

// Different backpressure strategies
source.onBackpressureBuffer(100) // Buffer up to 100 items
    .subscribe(System.out::println);

source.onBackpressureDrop() // Drop items when overwhelmed
    .subscribe(System.out::println);

source.onBackpressureLatest() // Keep only latest item
    .subscribe(System.out::println);

// Custom backpressure
source.onBackpressureBuffer(
    50,
    item -> System.out.println("Dropped: " + item),
    BufferOverflowStrategy.DROP_OLDEST
).subscribe(System.out::println);
```

### Hot vs Cold Streams

```java
// Cold stream - starts from beginning for each subscriber
Flux<String> coldStream = Flux.just("a", "b", "c");

// Hot stream - shares emissions between subscribers
ConnectableFlux<String> hotStream = Flux.just("a", "b", "c")
    .publish();
hotStream.connect(); // Start emitting

// Convert cold to hot
Flux<Long> shared = Flux.interval(Duration.ofSeconds(1))
    .share(); // Multiple subscribers share same sequence
```

---

## Kafka Integration

### Producer Setup

```java
@Configuration
public class KafkaProducerConfig {
    
    @Bean
    public ProducerFactory<String, Object> producerFactory() {
        Map<String, Object> props = new HashMap<>();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, 
                  StringSerializer.class);
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, 
                  JsonSerializer.class);
        props.put(ProducerConfig.ACKS_CONFIG, "all");
        props.put(ProducerConfig.RETRIES_CONFIG, 3);
        props.put(ProducerConfig.BATCH_SIZE_CONFIG, 16384);
        props.put(ProducerConfig.LINGER_MS_CONFIG, 1);
        return new DefaultKafkaProducerFactory<>(props);
    }
    
    @Bean
    public KafkaTemplate<String, Object> kafkaTemplate() {
        return new KafkaTemplate<>(producerFactory());
    }
}

@Service
public class EventPublisher {
    
    @Autowired
    private KafkaTemplate<String, Object> kafkaTemplate;
    
    public CompletableFuture<SendResult<String, Object>> publishEvent(
            String topic, String key, Object event) {
        return kafkaTemplate.send(topic, key, event);
    }
}
```

### Consumer Setup

```java
@Configuration
@EnableKafka
public class KafkaConsumerConfig {
    
    @Bean
    public ConsumerFactory<String, Object> consumerFactory() {
        Map<String, Object> props = new HashMap<>();
        props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(ConsumerConfig.GROUP_ID_CONFIG, "my-group");
        props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, 
                  StringDeserializer.class);
        props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, 
                  JsonDeserializer.class);
        props.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");
        props.put(ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG, false);
        props.put(JsonDeserializer.TRUSTED_PACKAGES, "*");
        return new DefaultKafkaConsumerFactory<>(props);
    }
    
    @Bean
    public ConcurrentKafkaListenerContainerFactory<String, Object> 
            kafkaListenerContainerFactory() {
        ConcurrentKafkaListenerContainerFactory<String, Object> factory = 
            new ConcurrentKafkaListenerContainerFactory<>();
        factory.setConsumerFactory(consumerFactory());
        factory.getContainerProperties()
               .setAckMode(ContainerProperties.AckMode.MANUAL_IMMEDIATE);
        return factory;
    }
}

@Component
public class EventConsumer {
    
    @KafkaListener(topics = "user-events", groupId = "user-service")
    public void handleUserEvent(
            @Payload UserEvent event,
            @Header(KafkaHeaders.RECEIVED_KEY) String key,
            Acknowledgment acknowledgment) {
        
        try {
            processUserEvent(event);
            acknowledgment.acknowledge();
        } catch (Exception e) {
            log.error("Failed to process event: {}", event, e);
        }
    }
}
```

### Kafka Streams

```java
@Configuration
@EnableKafkaStreams
public class KafkaStreamsConfig {
    
    @Bean(name = KafkaStreamsDefaultConfiguration
                 .DEFAULT_STREAMS_CONFIG_BEAN_NAME)
    public KafkaStreamsConfiguration kStreamsConfig() {
        Map<String, Object> props = new HashMap<>();
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, "streams-app");
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, 
                  Serdes.String().getClass());
        props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, 
                  Serdes.String().getClass());
        return new KafkaStreamsConfiguration(props);
    }
    
    @Bean
    public KStream<String, String> kStream(StreamsBuilder builder) {
        KStream<String, String> stream = builder.stream("input-topic");
        
        stream
            .filter((key, value) -> value.length() > 5)
            .mapValues(String::toUpperCase)
            .peek((key, value) -> System.out.println("Processing: " + value))
            .to("output-topic");
            
        return stream;
    }
}
```

---

## WebFlux Streaming

### Server-Sent Events

```java
@RestController
public class StreamController {
    
    @GetMapping(value = "/stream", 
                produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<String> streamData() {
        return Flux.interval(Duration.ofSeconds(1))
            .map(sequence -> "Data point: " + sequence)
            .take(100);
    }
    
    @GetMapping("/stream-objects")
    public Flux<ServerSentEvent<String>> streamEvents() {
        return Flux.interval(Duration.ofSeconds(1))
            .map(sequence -> ServerSentEvent.<String>builder()
                .id(String.valueOf(sequence))
                .event("message")
                .data("Event data: " + sequence)
                .build());
    }
}
```

### WebSocket Streaming

```java
@Configuration
@EnableWebSocket
public class WebSocketConfig implements WebSocketConfigurer {
    
    @Override
    public void registerWebSocketHandlers(WebSocketHandlerRegistry registry) {
        registry.addHandler(new StreamWebSocketHandler(), "/ws-stream")
            .setAllowedOrigins("*");
    }
}

public class StreamWebSocketHandler extends TextWebSocketHandler {
    
    private final Flux<String> dataStream = Flux.interval(Duration.ofSeconds(1))
        .map(i -> "Stream data: " + i);
    
    @Override
    public void afterConnectionEstablished(WebSocketSession session) {
        dataStream
            .map(data -> new TextMessage(data))
            .subscribe(message -> {
                try {
                    session.sendMessage(message);
                } catch (IOException e) {
                    log.error("Error sending message", e);
                }
            });
    }
}
```

### Reactive Database Access

```java
@Repository
public class PersonRepository {
    
    private final R2dbcEntityTemplate template;
    
    public Flux<Person> findAllByAgeGreaterThan(int age) {
        return template.select(Person.class)
            .matching(Query.query(Criteria.where("age").greaterThan(age)))
            .all();
    }
    
    public Flux<Person> streamAllPeople() {
        return template.select(Person.class)
            .all()
            .delayElements(Duration.ofMillis(100)); // Simulate streaming
    }
}

@Service
public class PersonService {
    
    public Flux<PersonDto> getAdultStream() {
        return personRepository.findAllByAgeGreaterThan(18)
            .map(this::toDto)
            .onErrorResume(throwable -> {
                log.error("Error in stream", throwable);
                return Flux.empty();
            });
    }
}
```

---

## Performance Tips

### Stream Optimization

```java
// Bad - Multiple terminal operations
list.stream().count(); // Creates new stream
list.stream().max(comparator); // Creates another new stream

// Good - Single pipeline
Optional<Integer> result = list.stream()
    .filter(Objects::nonNull)
    .map(String::length)
    .max(Integer::compareTo);

// Use primitive streams when possible
IntStream.range(1, 1000)
    .filter(i -> i % 2 == 0)
    .sum(); // Avoids boxing/unboxing

// Parallel streams for CPU-intensive tasks
List<ComplexResult> results = largeDataSet.parallelStream()
    .map(this::expensiveComputation) // CPU-bound operation
    .collect(Collectors.toList());
```

### Memory Management

```java
// Use lazy evaluation
Stream<String> lazyStream = Files.lines(Paths.get("largefile.txt"))
    .filter(line -> line.contains("search"))
    .map(String::trim);

// Limit infinite streams
Stream.iterate(0, n -> n + 1)
    .limit(1000) // Always limit infinite streams
    .forEach(System.out::println);

// Use try-with-resources for file streams
try (Stream<String> lines = Files.lines(path)) {
    lines.filter(line -> line.length() > 100)
        .forEach(System.out::println);
}
```

---

## Common Patterns

### Event Sourcing

```java
@Entity
public class EventStore {
    @Id
    private String id;
    private String aggregateId;
    private String eventType;
    private String eventData;
    private LocalDateTime timestamp;
    
    // getters/setters
}

@Service
public class EventSourcingService {
    
    public void appendEvent(String aggregateId, DomainEvent event) {
        EventStore eventStore = new EventStore();
        eventStore.setAggregateId(aggregateId);
        eventStore.setEventType(event.getClass().getSimpleName());
        eventStore.setEventData(objectMapper.writeValueAsString(event));
        eventStore.setTimestamp(LocalDateTime.now());
        
        eventRepository.save(eventStore);
        
        // Publish to stream
        kafkaTemplate.send("domain-events", aggregateId, event);
    }
    
    public Flux<DomainEvent> replayEvents(String aggregateId) {
        return eventRepository.findByAggregateIdOrderByTimestamp(aggregateId)
            .map(this::deserializeEvent);
    }
}
```

### CQRS with Streams

```java
// Command side
@Component
public class OrderCommandHandler {
    
    @EventListener
    public void handle(CreateOrderCommand command) {
        Order order = new Order(command.getCustomerId(), command.getItems());
        orderRepository.save(order);
        
        // Publish event
        OrderCreatedEvent event = new OrderCreatedEvent(order.getId(), 
            order.getCustomerId(), order.getTotalAmount());
        applicationEventPublisher.publishEvent(event);
    }
}

// Query side projection
@Component
public class OrderProjectionHandler {
    
    @EventListener
    public void on(OrderCreatedEvent event) {
        OrderView view = new OrderView();
        view.setOrderId(event.getOrderId());
        view.setCustomerId(event.getCustomerId());
        view.setAmount(event.getAmount());
        view.setStatus("CREATED");
        
        orderViewRepository.save(view);
    }
    
    @KafkaListener(topics = "order-events")
    public void handleOrderEvent(OrderEvent event) {
        updateOrderProjection(event);
    }
}
```

### Circuit Breaker Pattern

```java
@Component
public class ExternalServiceClient {
    
    private final CircuitBreaker circuitBreaker;
    
    public ExternalServiceClient() {
        this.circuitBreaker = CircuitBreaker.ofDefaults("externalService");
        circuitBreaker.getEventPublisher()
            .onStateTransition(event -> 
                log.info("Circuit breaker state transition: {}", event));
    }
    
    public Mono<String> callExternalService(String data) {
        return Mono.fromSupplier(() -> circuitBreaker.executeSupplier(() -> {
            return restTemplate.postForObject("/api/process", data, String.class);
        }))
        .onErrorReturn("Fallback response");
    }
}
```

---

## Testing Streams

### Testing Java Streams

```java
@Test
void testStreamProcessing() {
    List<Person> people = Arrays.asList(
        new Person("Alice", 25),
        new Person("Bob", 17),
        new Person("Charlie", 30)
    );
    
    List<String> adultNames = people.stream()
        .filter(p -> p.getAge() >= 18)
        .map(Person::getName)
        .collect(Collectors.toList());
    
    assertThat(adultNames)
        .hasSize(2)
        .containsExactly("Alice", "Charlie");
}
```

### Testing Reactive Streams

```java
@Test
void testReactiveStream() {
    Flux<String> source = Flux.just("a", "b", "c")
        .map(String::toUpperCase);
    
    StepVerifier.create(source)
        .expectNext("A")
        .expectNext("B")
        .expectNext("C")
        .verifyComplete();
}

@Test
void testStreamWithError() {
    Flux<String> source = Flux.just("a", "error", "c")
        .map(s -> {
            if ("error".equals(s)) {
                throw new RuntimeException("Test error");
            }
            return s.toUpperCase();
        })
        .onErrorReturn("FALLBACK");
    
    StepVerifier.create(source)
        .expectNext("A")
        .expectNext("FALLBACK")
        .verifyComplete();
}
```

### Testing Kafka Streams

```java
@SpringBootTest
@TestMethodOrder(OrderAnnotation.class)
class KafkaStreamsIntegrationTest {
    
    @Autowired
    private KafkaTemplate<String, String> kafkaTemplate;
    
    @Test
    @Order(1)
    void testKafkaStream() {
        // Send test data
        kafkaTemplate.send("input-topic", "key1", "hello world");
        
        // Verify processed data (would need test consumer)
    }
}
```

---

## Best Practices

### Stream Design Principles

```java
// 1. Prefer method references over lambdas when possible
list.stream()
    .map(String::toUpperCase)        // Good
    .filter(Objects::nonNull)        // Good
    .collect(Collectors.toList());

// 2. Use appropriate collectors
Map<String, List<Person>> grouped = people.stream()
    .collect(Collectors.groupingBy(Person::getCity));

// 3. Handle null values explicitly
Optional<String> result = list.stream()
    .filter(Objects::nonNull)
    .findFirst();

// 4. Use parallel streams judiciously
boolean shouldUseParallel = list.size() > 10000 && 
    isComputationIntensive(operation);

if (shouldUseParallel) {
    list.parallelStream().map(operation).collect(toList());
} else {
    list.stream().map(operation).collect(toList());
}
```

### Error Handling

```java
// Reactive streams error handling
public Flux<ProcessedData> processDataStream(Flux<RawData> input) {
    return input
        .onErrorMap(IOException.class, 
                   ex -> new ProcessingException("IO error", ex))
        .retry(3)
        .onErrorReturn(ProcessedData.empty())
        .timeout(Duration.ofSeconds(30))
        .onErrorResume(TimeoutException.class, 
                      ex -> Flux.just(ProcessedData.timeout()));
}

// Traditional streams with try-catch
public List<Result> processWithErrorHandling(List<Input> inputs) {
    return inputs.stream()
        .map(input -> {
            try {
                return processInput(input);
            } catch (Exception e) {
                log.warn("Failed to process input: {}", input, e);
                return Result.failed(input);
            }
        })
        .filter(Result::isSuccess)
        .collect(Collectors.toList());
}
```

### Resource Management

```java
// Always close resources
try (Stream<String> lines = Files.lines(path)) {
    return lines
        .filter(line -> line.startsWith("ERROR"))
        .collect(Collectors.toList());
} catch (IOException e) {
    throw new ProcessingException("Failed to read file", e);
}

// Proper disposal of reactive streams
@PreDestroy
public void cleanup() {
    if (subscription != null) {
        subscription.dispose();
    }
}
```

---

## Quick Reference

### Stream Operations Cheat Sheet

```java
// Intermediate Operations (lazy)
.filter(predicate)           // Keep elements matching condition
.map(function)              // Transform elements
.flatMap(function)          // Transform and flatten
.distinct()                 // Remove duplicates
.sorted()                   // Sort elements
.peek(consumer)             // Perform action without changing stream
.limit(n)                   // Take first n elements
.skip(n)                    // Skip first n elements

// Terminal Operations (eager)
.forEach(consumer)          // Perform action on each element
.collect(collector)         // Collect to collection/map/etc
.reduce(accumulator)        // Reduce to single value
.count()                    // Count elements
.anyMatch(predicate)        // Check if any element matches
.allMatch(predicate)        // Check if all elements match
.findFirst()               // Get first element (Optional)
.findAny()                 // Get any element (Optional)
.min(comparator)           // Find minimum (Optional)
.max(comparator)           // Find maximum (Optional)
```

### Reactive Operators Cheat Sheet

```java
// Creation
Flux.just(1, 2, 3)
Flux.fromIterable(list)
Flux.range(1, 10)
Flux.interval(Duration.ofSeconds(1))

// Transformation
.map(x -> x * 2)
.flatMap(x -> processAsync(x))
.filter(x -> x > 0)
.take(10)
.skip(5)

// Combination
.merge(otherFlux)
.zip(otherFlux)
.concat(otherFlux)

// Error Handling
.onErrorReturn("default")
.onErrorResume(fallbackFlux)
.retry(3)
.timeout(Duration.ofSeconds(5))

// Side Effects
.doOnNext(System.out::println)
.doOnError(error -> log.error("Error", error))
.doOnComplete(() -> log.info("Completed"))
```

### Common Collectors

```java
// Basic collections
.collect(Collectors.toList())
.collect(Collectors.toSet())
.collect(Collectors.toMap(keyMapper, valueMapper))

// Grouping and partitioning
.collect(Collectors.groupingBy(classifier))
.collect(Collectors.partitioningBy(predicate))

// Statistical operations
.collect(Collectors.counting())
.collect(Collectors.averagingDouble(mapper))
.collect(Collectors.summarizingInt(mapper))

// String operations
.collect(Collectors.joining())
.collect(Collectors.joining(", "))
.collect(Collectors.joining(", ", "[", "]"))
```

---

*Happy Streaming! 🚀*

**Author:** Mohammad S Hossain