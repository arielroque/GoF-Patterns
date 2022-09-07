# Singleton Pattern

Singleton provides a mechanism to have **one, and only one, object** of a give type and provides **global point of access**. Hence, Singletons are typically used in cases such as logging and database operations where there is only one instance of the object to avoid conflicting requests.

In breaf, the intentions of the Singleton design pattern are as follows:

 - Ensuring that one and only one object of the class gets created
 - Controlling concurrent access to resources that are shared
 - Providing an method to access an object that is global

## Implementations

### Classical Singleton

- Here, we override the **__new__** method (special method responsible to instantiate objects) to control the object creation
- The ```hasattr``` method is used to verify if the object have an instance property
- See the code [here](classical_singleton.py)

### Singleton with Metaclasses

- Metaclasses are a way to tell how the object must behave in a moment 
- Here, we using metaclass overriding the **__call__** (special method callend when a object needs to be created for an already existing class)
- If a instance is not in the ```instances```dictionary, we add
- See the code [here](singleton_using_metaclasse.py)

### Real Example 

- Consider a cloud service is split across multiple services that perform a database operations
- We need take care of consistency across operations (conflict operations) and optimal utilization of memory and CPU
- See the code [here](real_example.py)