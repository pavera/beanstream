'''
Copyright 2012 Upverter Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

from datetime import date

def process_date(datestring):
    """ 11/29/2011 --> date(2011, 11, 29) """
    month, day, year = datestring.split('/')
    return date(int(year), int(month), int(day))
