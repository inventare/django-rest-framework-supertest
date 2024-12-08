# django-rest-framework-supertest

An **WORK IN PROGRESS** set of utilities to write automated tests for APIS writen in django-rest-framework.

<p align="center">
    <a href='https://github.com/inventare/django-rest-framework-supertest/actions/workflows/tests.yml'><img alt="GitHub Workflow Status (with event)" src="https://img.shields.io/github/actions/workflow/status/inventare/django-rest-framework-supertest/tests.yml?label=tests" /></a>
    <a href='https://coveralls.io/github/inventare/django-rest-framework-supertest?branch=main'><img src='https://coveralls.io/repos/github/inventare/django-rest-framework-supertest/badge.svg?branch=main' alt='Coverage Status' /></a>
</p>

## Motivation

The **django** and **django-rest-framework** provides a powerfull set of tools to create **Web Applications** and **REST API's**. Testing these **API's** with automated tests are a little bit more complex question with the necessity of write a bunch of repeated code and made all assertions is, some times, hard. This project wants to aggregate some utilities to turns the testing on projects with **django-rest-framework** a little bit easy.

## Goals

The main goal of this project is to help to write tests in various types of applications: a new project using TDD or a old, in production, application. Based on it, we decided to write all the package around the original django testing library unittest.

## Under the Hood

Under the hood, this is only an set of utilities and this uses some libraries to work correctly. Actually, for fake data generation we use [Faker](https://faker.readthedocs.io/en/master/index.html), with some small custom provider's. For assertions, we use the default **django** and **django-rest-framework** `unittest` features. We provide some **mixins** with our own methods and some base `classes`.

### Optional dependencies

The project has out of box support for some things, like the SimpleJWT authentication that depends on third party packages. This should be described in the future documentations.

## Currently Roadmap to Future

- [x] Add Basic Faker Support.
- [x] Assertions APIExceptions.
- [x] Assert Validation Errors.
- [x] Create Faker Shortcuts.
- [x] Work with images and files.
- [x] Assert Serializer Responses.
- [x] Work with multiple types of Authentication.
- [ ] Work with pagination.
- [ ] Work with default TokenAuthentication.
- [ ] Validate the Work with a custom authentication system.
- [ ] Validate serializer and json response.
- [ ] Write documentation about this library.

> This is an incomplete roadmap and, before the first version release, some new items can be added here.
