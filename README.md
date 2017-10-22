# ds2016
Some files about the final project of Data Structure 2016 Spring

## Include
- Headers
- Testcases
- Documentation
- Statements

## Compile Command

`g++ $(TEST_NAME).cc -o $(TEST_NAME) -O2 -std=c++11`

## F.A.Q.

- Q: Can I add some other constructors for iterators?
- A: Of course. You can add everything you want but you can not delete any functions in the original files.

- Q: Can I rewrite some operators as friend functions?
- A: Yes, but it may cause some errors.

## Hints
### Placement new expression
#### format of expression
```::(optional) new (placement_params)(optional) ( type ) initializer(optional)```
or
```::(optional) new (placement_params)(optional) type initializer(optional)```
#### operator new
replaceable allocation functions
```void* operator new  ( std::size_t count );
void* operator new[]( std::size_t count );
void* operator new  ( std::size_t count, const std::nothrow_t& tag);
void* operator new[]( std::size_t count, const std::nothrow_t& tag);```
placement allocation functions
```void* operator new  ( std::size_t count, void* ptr );
void* operator new[]( std::size_t count, void* ptr );
void* operator new  ( std::size_t count, user-defined-args... );
void* operator new[]( std::size_t count, user-defined-args... );```	
class-specific allocation functions
```void* T::operator new  ( std::size_t count );
void* T::operator new[]( std::size_t count );
void* T::operator new  ( std::size_t count, user-defined-args... );
void* T::operator new[]( std::size_t count, user-defined-args... );```
### free() or delete expression





