#!/usr/bin/env python3

#Copyright (c) 2010 Dimitris Leventeas <mydimle@gmail.com>

#Permission is hereby granted, free of charge, to any person
#obtaining a copy of this software and associated documentation
#files (the "Software"), to deal in the Software without
#restriction, including without limitation the rights to use,
#copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the
#Software is furnished to do so, subject to the following
#conditions:

#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.

from optparse import OptionParser
from xml.etree.cElementTree import ElementTree, Element
import pywapi

def write_everything_from_yahoo_to_xml(country, cities, outfile='weather.xml'):
    """ Write all the results from google to an xml file """
    weather_reports = pywapi.get_everything_from_yahoo(country, cities)
    
    xml_output = Element('Weather')
    for city, report in weather_reports.items():
        try:
            xml_city = Element('town')
            
            xml_name = Element('name')
            xml_name.text = city
            xml_city.append(xml_name)
            
            xml_temperature = Element('temperature')
            temp_c = report['wind']['chill']
            temp_unit = report['units']['temperature']
            temp_cond = ''.join([temp_c, ' ', temp_unit])
            xml_temperature.text = temp_cond
            xml_city.append(xml_temperature)
            
            xml_humidity = Element('humidity')
            xml_humidity.text = report['atmosphere']['humidity']
            xml_city.append(xml_humidity)
            
            xml_condition = Element('condition')
            xml_condition.text = report['condition']['text']
            xml_city.append(xml_condition)
            
            xml_wind = Element('wind')
            beaufort = pywapi.wind_beaufort_scale(report['wind']['speed'])
            direction = pywapi.wind_direction(report['wind']['direction'])
            wind_cond = ''.join([beaufort, ' ', direction])
            xml_wind.text = wind_cond
            xml_city.append(xml_wind)
            
            xml_output.append(xml_city)
        except KeyError:
            pass
        
    ElementTree(xml_output).write(outfile, 'UTF-8')

def main():
    parser = OptionParser(\
        usage='Collect information about the weather in Greece.')
    parser.add_option("-f", "--file", dest="filename", default="weather.xml",\
        help="write directory contents to FILE (default: weather.xml)",\
        metavar="FILE")

    (options, args) = parser.parse_args()

    # Greece (GRXX) has 81 cities available with data
    write_everything_from_yahoo_to_xml('GRXX', 81, outfile=options.filename)
    
if __name__ == '__main__':
    main()
