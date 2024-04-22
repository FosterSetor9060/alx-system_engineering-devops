#!/usr/bin/pup
# Ensuring that Flask version 2.1.0 is installed.
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
