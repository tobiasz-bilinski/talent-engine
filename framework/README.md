# Project title

Testing framework (Talent Engine 2.0)

## About

This project is a testing framework that utilizes Pytest.

## Dependencies

Required modules are specified in requirements.txt

```
pip install -r requirements.txt
```

## Running the tests

To run the tests run `pytest` from the root folder.

## Structure of the framework

envs_configs - stores configuration data  
src/config - sets up configuration for the framework (connection with providers, location of test data etc.).

- config.py: contains Config class. When instantiated, it creates the config dictionary ('conf_dict') and using the '\_register' method receives the data from the providers and stores it in the config dictionary (raising ValueError if the item is not present in any of the providers). The 'get' method retrieves the data stored in config dictionary. When creating an instance of the Config class, config providers must be passed in as a list in a hierarchical order:

  ```
  config = Config([JSONConfigProvider, OSConfigProvider])
  ```

  In the above example, the '\_register' method called during instantiation will first look for the item in JSONConfigProvider, and if it's not present, it will look in OSConfigProvider.

- config_providers.py: contains classes for config providers (OSConfigProvider and JSONConfigProvider), as well as a BaseProviderClass, which raises an exception if 'get' method is not implemented in the child class. All config provider classes must inherit from BaseProviderClass.
  - OSConfigProvider: - 'get' returns the value of specified environment variable or None if it doesn't exist.
  - JSONConfigProvider: - '\_read_config' returns a dictionary with the contents of JSON file with path 'config_path' - 'get' returns the value of specified item in dictionary received from '\_read_config'. The JSON file should be located in /envs_configs directory. **Absolute path** to JSON file needs to be passed in:
  ```
    value = JSONConfigProvider.\_read_config(insert_absolute_path_to_json_file_here)
  ```
    
  
src/data - contains test data  
src/models - contains models  
src/providers - contains config providers
