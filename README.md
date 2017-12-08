# Bolt Message Bus

## Introduction
Bolt Message Serves the purpose of transmission control of messages from the Bolt Server to the Bolt Clients and Vice Versa. This allows for a centralized stream for data transmission across the various components of the Bolt ecosystem while the server schedules the various tasks.

## Communication Overview
Bolt uses UDP communication to transmit the data between the different components of the ecosystem. The acknowledgements happen by the client as soon as the task finishes.

## Current Development Status
Planning