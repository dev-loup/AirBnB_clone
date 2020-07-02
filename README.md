[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# HBNB - The AirBnb Clone V 1.0
<p align="center">
  <img src="/misc/HBNB.png" alt="bash" width="350" height="150">

HBNB clone takes AirBnb original Web page and services for making a full functional Service, back-end and front-end are implemented from scratch following this structure:

<p align="center">
  <img src="/misc/scheme.png" alt="bash" width="700" height="325">
</p>

## Getting started 

* HBNB system manages front-end site appeareance, back-end manages data persistance and JSON manipulation, APi's for interacting with HBNB will be developed in future releases

Inside the repository execute:

```bash
./console.py
```

## Usage

### Invocation

* in non interactive mode from SH:

```bash
$> echo "help" | ./console.py
>custom help response<
$>
```

* In interactive mode:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

* Going out interactive mode

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Road Map

* [OK] A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* [__] A website (the front-end) that shows the final product to everybody: static and dynamic
* [OK] A database or files that store data (data = objects)
* [__] An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Contributing
Pull requests and reporting issues are always welcome, make a pull request for contacting us :)

## License

Educational purposes, content is not licensed and it does not have technical support

[contributors-shield]: https://img.shields.io/github/contributors/diego-9407/AirBnB_clone?style=flat-square
[contributors-url]: https://github.com/diego-9407/AirBnB_clone/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/diego-9407/AirBnB_clone.svg?style=flat-square
[forks-url]: https://github.com/diego-9407/AirBnB_clone/network/members
[stars-shield]: https://img.shields.io/github/stars/diego-9407/AirBnB_clone.svg?style=flat-square
[stars-url]: https://github.com/diego-9407/AirBnB_clone/stargazers
[issues-shield]: https://img.shields.io/github/issues/diego-9407/AirBnB_clone?style=flat-square
[issues-url]: https://github.com/diego-9407/AirBnB_clone/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/diegromero