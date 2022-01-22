# Zapier Backend Engineering Skills Interview

## Project Details

Please consider this document as a set of requirements and deliver the code necessary to fulfill these requirements. If a requirement seems ambiguous, state your understanding of the requirements in a readme or inline comments along with your solution.

We use this project to understand how you break a problem down and solve it with code. Please **do not** submit a solution with code snippets you find on the internet as this does not help us understand your programming skill.

## Scenario

Your mission is to build a portion of a billing system for a fictional cloud service provider. You are on the billing team at this company and need to provide a system that allows other teams at the company to add line items to customers' invoices.

## Deliverables

There are three deliverables for this project:

1. An internal web service API for managing invoices
1. A client library that wraps the internal web service API. This would be the client used by other teams to interact with the API
1. A test suite to validate the web service and library work as expected

## Specs


### General

* You may implement the project in any language you choose.
* You may use any framework, such as a web framework or test framework, to help you complete the project.
* You may store the data for this system in any database you choose.
* You may model the data any way you'd like, including adding data beyond the samples provided.

### Web Service

* Your service should implement a single endpoint that accepts POST requests.
* Your service should add line items to a customer's current invoice.
* Your service should handle edge cases appropriately and return appropriate HTTP status codes.
* Your service should have at least one test.

### Library

* Your library should be a client for the internal web service, wrapping the available endpoint.
* Your library should encode safe usage of the internal web service, protecting against scenarios like adding duplicate invoice items.
* Your library should handle other edge cases appropriately (i.e. raising an exception or retrying requests).
* Your library should be safe to exeucte in a multi-threaded or distributed environment.
* Your library should have at least one test.

As a reminder, here is [the gist with examples](https://gist.github.com/zapier-interviews/7c7e405d2b7b50e2b27c2ce6e04b9dc2) of how another team at your company would potentially use your library.

## Sample Data

Below is some sample data you can use to populate your database. Feel free to extend or modify this data for your project:

Customers

```json
[
  {
    "id": 123,
    "name": "Alice"
  },
  {
    "id": 456,
    "name": "Bob"
  },
  {
    "id": 789,
    "name": "Taylor"
  }
]
```

Line Items

```json
[
  {
    "customerId": 123,
    "service": "Database Hosting",
    "unitsConsumed": 58,
    "pricePerUnit": 0.05
  },
  {
    "customerId": 456,
    "service": "Load Balancer",
    "unitsConsumed": 27,
    "pricePerUnit": 0.03
  },
  {
    "customerId": 123,
    "service": "Linux Instance",
    "unitsConsumed": 42,
    "pricePerUnit": 0.15
  },
  {
    "customerId": 123,
    "service": "CDN Storage",
    "unitsConsumed": 15,
    "pricePerUnit": 0.02
  },
  {
    "customerId": 456,
    "service": "Domain Name Registration",
    "unitsConsumed": 1,
    "pricePerUnit": 14.99
  },
]
```

## Project Time Limit

Please do not spend more than **2.5 hours** on the project.

Be sure to commit your code regularly as you work through your solution. This is helpful for us to understand how you work. At the very least, you must commit and push to GitHub once during the project or we will not be able to score your solution.

**Commits after the time limit will not be scored.** Think you might go over time? Don't worry! Wrap up and commit what you've got. We will still review everything up to the limit.

## Once Finished

To deliver your project, you will create a pull request (see below) and submit the URL to us via the greenhouse.io link you received by email.

Commit your final work and push to the `project` branch of the private GitHub repo provided by Zapier. 

Open a pull request to merge your `project` branch to `master`. Time spent opening up the pull request will **not** count as part of your project time. Feel free to take a break and come back to this, but please open your PR within one day.

As part of the pull request, use the description and/or comments on the PR to tell us:

  * A description of your solution at a high-level, including language used, framework used, roughly how it works, etc.
  * What trade-offs you made
  * Any assumptions you made that affected your solution
  * What changes would you make if you had more time
  * What you would change if you built this for production
  * Brief instructions on how to setup the environment to run your project

If you finish early and want to submit unfinished ideas, please add those to other branches.

When the PR is ready, submit the URL to your greenhouse.io link. You will find the Greenhouse link in the previous email inviting you to take the skill test.

## How We'll Review Your Pull Request

Once complete, we'll review your pull request for:

* **Communication** - How effectively you communicate about code through the PR description, readme, and any comments.
* **Solution Design** - How you decided to solve this problem.
* **Completeness** - How much of the spec you were able to implement.
* **Clarity** - How well we can understand your code and the decisions you made in the implementation.

Note that code style does not factor much into the scoring. We understand this is a high pressure, time-boxed exercise. We are more interested in how you problem solve and communicate than write code that adheres to a particular style.
