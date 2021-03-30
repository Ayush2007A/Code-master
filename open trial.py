Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> open("astroML", "a")
<_io.TextIOWrapper name='astroML' mode='a' encoding='cp1252'>
>>> cosmology
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    cosmology
NameError: name 'cosmology' is not defined
>>> from astroML open("cosmology", "a")
SyntaxError: invalid syntax
>>> open ("cosmology", "a")
<_io.TextIOWrapper name='cosmology' mode='a' encoding='cp1252'>
>>> print 'a'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('a')?
>>> print ('A')
A
>>> 