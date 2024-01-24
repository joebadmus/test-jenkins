@test
Feature: Test Feature

    Scenario: Deal initial cards
        Given a dealer
        When the round starts
        Then the dealer gives itself two cards