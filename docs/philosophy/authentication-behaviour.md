# Authentication Behaviour

This text introduces our philosophy about authentication behaviour testing inside django REST API's.

## Introduction

The `APIClient` present at the `APITestCase` of the **django** and **django-rest-framework** provides two methods to work with authentication: `login()` and `force_login()` with two different behaviours. The first method uses the configured django authentication back-end's (equivalent of adapter design pattern, for non-django developers).

As, we comented above, this methods uses the default **django** session authentication, because those methods are writen by default client and not by **django-rest-framework** or by **djangorestframework-simplejwt**, for jwt authentication-based API's.

For example, this methods are good mehtods for testing the **django-admin** Ajax API Views, like the `AutocompleteJsonView` ([ref](https://github.com/django/django/blob/main/django/contrib/admin/views/autocomplete.py#L8C7-L8C27)) but are not effective for testing API's with JWT, Basic or Token model authentication-based API's.

## Our Philosophy

Our philosophy about testing with JWT Authentication, or other Authorization header based method, is test all the behaviour of authentication inside the aplication with real use-cases. To made this work a little bit easy, we decided to introduce **authentication** helpers for the `APITestCase`.

The helper is configurable and the agnostic methods and assertions are defined inside an mixin.

## Techinical Part
---

TODO: write technical part for this text.
