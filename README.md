# django-rest-framework-supertest

An **WORK IN PROGRESS** set of utilities to write automated tests for APIS writen in django-rest-framework.

<p align="center">
    <a href='https://github.com/inventare/django-rest-framework-supertest/actions/workflows/tests.yml'><img alt="GitHub Workflow Status (with event)" src="https://img.shields.io/github/actions/workflow/status/inventare/django-rest-framework-supertest/tests.yml?label=tests" /></a>
    <a href='https://coveralls.io/github/inventare/django-rest-framework-supertest?branch=main'><img src='https://coveralls.io/repos/github/inventare/django-rest-framework-supertest/badge.svg?branch=main' alt='Coverage Status' /></a>
    <a href="https://github.com/astral-sh/ruff"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff" style="max-width:100%;"></a>
</p>

## Motivation

The **django** and **django-rest-framework** is an powerfull set of tools to create **REST API's**. But, testing these **API'**, with automated tests, are a little more complex question. Write a lot of repeated code and the difficult to made all assertions along the **REST API's** responses is some of these problems for our apps.

This project wants to aggregate utilities to made assertions on the responses, like **APIException** responses, and utilities to work with other complex **REST API's** concepts, like pagination and authentication.

## Under the Hood

Under the hood, this is only an set of utilities and this uses some libraries to work correctly. Actually, for fake data generation we use [Faker](https://faker.readthedocs.io/en/master/index.html), with some small custom provider's. For assertions, we use the default **django** and **django-rest-framework** `unittest` features. We provide some **mixins** with our own methods and some base `classes`.

## Roadmap

- [x] Add Basic Faker Support
- [x] Assertions APIExceptions
- [x] Assert Validation Errors
- [x] Create Faker Shortcuts
- [x] Work with images and files
- [x] Assert Serializer Responses
- [ ] Work with pagination
- [ ] Work with multiple types of Authentication

> This is an basic roadmap for the first version and, before the first version release, some new itens can be added here.
