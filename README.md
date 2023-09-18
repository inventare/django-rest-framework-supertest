# django-rest-framework-supertest

An **WORK IN PROGRESS** set of utilities to write automated tests for APIS writen in django-rest-framework.

## Motivation

The **django** and **django-rest-framework** is an powerfull set of tools to create **REST API's**. But, testing these **API'**, with automated tests, are a little more complex question. Write a lot of repeated code and the difficult to made all assertions along the **REST API's** responses is some of these problems for our apps.

This project wants to aggregate utilities to made assertions on the responses, like **APIException** responses, and utilities to work with other complex **REST API's** concepts, like pagination and authentication.

## Under the Hood

Under the hood, this is only an set of utilities and this uses some libraries to work correctly. Actually, for fake data generation we use [Faker](https://faker.readthedocs.io/en/master/index.html), with some small custom provider's. For assertions, we use the default **django** and **django-rest-framework** `unittest` features. We provide some **mixins** with our own methods and some base `classes`.

## Roadmap

- [x] Add Basic Faker Support
- [x] Assertions APIExceptions
- [ ] Assert Validation Errors
- [ ] Assert Serializer Responses
- [ ] Work with multiple types of Authentication
- [ ] Work with pagination
- [ ] Work with images
- [ ] Create Faker Shortcuts

> This is an basic roadmap for the first version and, before the first version release, some new itens can be added here.