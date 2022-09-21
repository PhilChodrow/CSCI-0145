def convert_temp(degrees_f):
    """
    convert degrees fahrenheit to degrees celsius
    """
    degrees_c = (degrees_f - 32) / 1.8
    return degrees_c

def display(degrees_c):
    """
    print a simple string informing the user of the temperature in
    degrees celsius. Temperature is supplied in degrees celsius. 
    """
    print("It is now " + str(degrees_c) + " degrees Celsius.")
    
def display_f(degrees_f):
    """
    print a simple string informing the user of the temperature in
    degrees celsius. Temperature is supplied in degrees fahrenheit. 
    """
    degrees_c = convert_temp(degrees_f)
    display(degrees_c)
    
