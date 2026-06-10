# AI Sales Calling Agent

> An intelligent voice calling agent that automates real-time customer interactions by combining Twilio Voice API and Google Gemini AI — handling sales conversations, resolving queries, delivering product information, and processing bookings through natural speech.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Running the Application](#running-the-application)
- [Usage](#usage)
- [Modules](#modules)
- [Roadmap](#roadmap)
- [Author](#author)

---

## Overview

The AI Sales Calling Agent enables businesses to automate inbound and outbound phone interactions without sacrificing conversational quality. Powered by a Gemini-backed reasoning layer, the system dynamically adapts to customer intent — qualifying leads, answering product questions, and completing bookings in real time.

---

## Features

- AI-driven voice conversations with natural language understanding
- Automated handling of both inbound and outbound calls
- Real-time customer query resolution powered by Google Gemini
- Dynamic sales pitch generation based on conversation context
- Product and service information retrieval via knowledge base
- Appointment and course booking support
- Sales intelligence for lead qualification and intent analysis
- Webhook-based communication architecture with Twilio
- Local development support via ngrok tunnel

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Voice & Telephony | Twilio Voice API |
| AI / LLM | Google Gemini API |
| Tunneling | ngrok |
| Data Storage | JSON |
| Communication | REST APIs, Webhooks |

---

## Architecture

```
Customer Call
     │
     ▼
Twilio Voice API
     │  (webhook)
     ▼
Flask Backend (app.py)
     │
     ├──▶ Gemini AI        → Generates context-aware responses
     ├──▶ Sales Intelligence → Analyzes intent, qualifies leads
     ├──▶ Knowledge Base    → Retrieves business information
     └──▶ Booking System    → Processes appointments & registrations
     │
     ▼
Response delivered to caller via Twilio Voice
```

1. A customer initiates or receives a call through Twilio.
2. Twilio forwards events to the Flask backend via webhooks.
3. The backend extracts and processes the customer's input.
4. Gemini AI generates a context-aware, conversational response.
5. The sales intelligence module evaluates intent and lead signals.
6. Booking and knowledge modules inject relevant business data.
7. The final response is delivered to the caller through Twilio Voice.

---

## Project Structure

```
AI-Sales-Calling-Agent/
│
├── static/                   # Static assets (CSS, JS, images)
├── templates/                # HTML templates
│
├── app.py                    # Main Flask application & route definitions
├── call.py                   # Inbound/outbound call handling logic
├── booking_system.py         # Appointment booking management
├── course_booking.py         # Course registration functionality
├── knowledge_base.py         # Knowledge base integration layer
├── question_answerer.py      # Gemini-powered Q&A module
├── sales_intelligence.py     # Intent analysis & lead qualification engine
├── run_ngrok.py              # ngrok tunnel automation script
│
├── student_bookings.json     # Persistent booking data store
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variable template
└── .gitignore
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- A [Twilio](https://www.twilio.com) account with a provisioned phone number
- A [Google Gemini](https://aistudio.google.com) API key
- [ngrok](https://ngrok.com) installed (for local development)

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/meghana-22-11/AI-Sales-Calling-Agent.git
cd AI-Sales-Calling-Agent
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

### Configuration

Copy the environment variable template and populate it with your credentials:

```bash
cp .env.example .env
```

```env
GEMINI_API_KEY=your_gemini_api_key
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_number
```

### Running the Application

**Start the Flask server**

```bash
python app.py
```

**Expose your local server via ngrok**

```bash
python run_ngrok.py
# or
ngrok http 5000
```

**Configure the Twilio webhook**

In your [Twilio Console](https://console.twilio.com), set the Voice webhook URL for your phone number to:

```
https://<your-ngrok-subdomain>.ngrok-free.app/voice
```

---

## Usage

Once the server is running and the webhook is configured:

1. Call your Twilio phone number.
2. Interact naturally — ask questions about services, request pricing, or initiate a booking.
3. The AI agent responds in real time with contextually relevant, conversational answers.
4. Booking confirmations and lead data are persisted to `student_bookings.json`.

---

## Modules

### `call.py` — Call Management
Orchestrates the lifecycle of inbound and outbound voice calls using the Twilio Voice API, including TwiML response generation.

### `question_answerer.py` — AI Question Answering
Interfaces with Google Gemini to generate intelligent, context-aware responses to customer queries in real time.

### `knowledge_base.py` — Knowledge Base
Stores and retrieves structured business information (services, pricing, FAQs) to ground AI responses in accurate data.

### `booking_system.py` / `course_booking.py` — Booking Engine
Handles appointment scheduling, course registrations, and booking confirmations, persisting records to local JSON storage.

### `sales_intelligence.py` — Sales Intelligence
Analyzes conversation context to detect customer intent, surface buying signals, and support lead qualification decisions.

---

## Roadmap

- [ ] Multi-language support
- [ ] CRM integration (Salesforce, HubSpot)
- [ ] Call recording and transcription
- [ ] Automated lead scoring system
- [ ] WhatsApp channel integration
- [ ] Sentiment analysis during live calls
- [ ] Voice cloning and persona customization
- [ ] Real-time conversation monitoring dashboard

---

## Author

**Meghana**

---

*Built with [Twilio](https://www.twilio.com) · [Google Gemini](https://deepmind.google/technologies/gemini/) · [Flask](https://flask.palletsprojects.com)*
