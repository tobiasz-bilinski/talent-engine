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

/conftest.py - provides Pytest fixtures for the framework  
/envs_configs - stores configuration data  
/tests - stores the tests  
/src/applications - stores classes for applications
/src/config - sets up configuration for the framework (connection with providers, location of test data etc.).

- config.py: contains Config class. When instantiated, it creates the config dictionary (_'conf_dict'_) and using the _'\_register'_ method receives the data from the providers and stores it in the config dictionary (raising ValueError if the item is not present in any of the providers). The _'\_\_getattr\_\_'_ method retrieves the data stored in config dictionary. When creating an instance of the Config class, config providers must be passed in as a list in a hierarchical order:

  ```
  config = Config([JSONConfigProvider, OSConfigProvider])
  ```

  In the above example, the _'\_register'_ method called during instantiation will first look for the item in JSONConfigProvider, and if it's not present, it will look in OSConfigProvider.

  All config data **must** be registered using the _'\_register'_ method before it can be used.

src/data - contains test data, json schemas, URLs etc.
src/models - contains models
src/providers - contains config providers

- base*provider.py: contains a BaseProviderClass, which raises an exception if *'\_\_getitem\_\_'\_ method is not implemented in the child class. **All config provider classes must inherit from BaseProviderClass.**
- os*config_provider.py: - contains an OSConfigProvider class. method *'\_\_getitem\_\_'\_ returns the value of specified environment variable (or None if it doesn't exist).
- json*config_provider.py: - contains a JSONConfigProvider class. method *'\_read*config'* returns a dictionary with the contents of JSON file with path 'config*path' - *'\_\_getitem\_\_'_ returns the value of specified item in dictionary received from _'\_read*config'*. The JSON file should be located in the /envs_configs directory. **Absolute path** to JSON file needs to be passed in:

```
  value = JSONConfigProvider.\_read_config(insert_absolute_path_to_json_file_here)
```

## Author

Tobiasz Biliński - tobiasz.bilinski@globallogic.com
