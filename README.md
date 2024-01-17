## LAB - Class 04
- Project: pythonic-garage-band

- Author: DeAndre Ordonez

### Links and Resources - N/A
### Setup - N/A
### PORT - N/A
### DATABASE_URL - N/A
### How to initialize/run your application - python test_band.py
### How to use your library - N/A
Tests
### How do you run tests?

**Using pytest, provided functions in test_band.py to test the classes in band.py .**

- **Tested**

        test_guitarist_str - Tested Guitarist class and str method, returned expected
        
        test_guitarist_repr - Tested Guitarist class and repr method, returned expected

        test_drummer_str - Test Drummer class and str method, returned expected

        test_drummer_repr - Tested Guitarist class and repr method, returned expected

        test_bassist_str - Test Bassist class and str method, returned expected

        test_bassist_repr - Tested Bassist class and repr method, returned expected

        test_band_name - Tested Band class, returned expected name

        test_guitarist - Tested Guitarist class and get_instrument() method, returned expected

        test_bassist -Tested Bassist class and get_instrument() method, returned expected

        test_drummer -Tested Drummer class and get_instrument() method, returned expected

        test_instruments - Tested one_band() fixture, provided members and assigned instruments

        test_individual_solos -Tested one_band() fixture, tested play_solo method in respective classes

        test_band_members - Tested one_band() fixture, tested to see if members were instanced
        
        test_play_solos_for_whole_band -  Tested one_band() fixture, Tested play_solo methods in respective classes and returned the proper values

        test_class_tracks_instances - Tested reset_band(), previous instances were cleared, allowing only one instance to be stored

        test_to_list - Tested reset_band(), previous instances were cleared


### Any tests of note?

The fixture ones were interesting in following the process in how they worked

### Describe any tests that you did not complete, skipped, etc

Stretch Goals