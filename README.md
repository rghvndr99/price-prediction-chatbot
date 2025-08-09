# Price Prediction Chatbot

A comprehensive machine learning project for house price prediction with an agentic AI interface built using the Model Context Protocol (MCP).

## Overview

This repository contains a complete house price prediction system that combines machine learning models with an intelligent agent interface. The system can predict house prices based on various property features like location, number of bedrooms, bathrooms, and area.

## Repository Structure

```
price-prediction-chatbot/
├── price-prediction-agentic-ai/    # Main MCP server application
│   ├── main.py                     # MCP server implementation
│   ├── model/                      # ML models and data
│   ├── pyproject.toml              # Project configuration
│   └── README.md                   # Detailed documentation
├── requirements.txt                # Python dependencies
├── util.py                         # Utility functions for model operations
├── test_dependencies.py            # Dependency testing script
├── .gitignore                      # Git ignore rules
└── README.md                       # This file
```

## Components

### 1. MCP Server (`price-prediction-agentic-ai/`)

The main application built with FastMCP that provides:
- Real-time house price prediction API
- MCP-compatible tools for AI agent integration
- Resource endpoints for dynamic content

### 2. Utility Functions (`util.py`)

Core machine learning utilities including:
- Model loading and initialization
- Price prediction logic
- Location data handling

### 3. Testing (`test_dependencies.py`)

Dependency validation and testing utilities to ensure all required packages are properly installed.

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd price-prediction-chatbot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Navigate to the main application:**
   ```bash
   cd price-prediction-agentic-ai
   ```

4. **Start the MCP server:**
   ```bash
   python main.py
   ```

## Features

- **🏠 House Price Prediction**: ML-powered price estimation based on property features
- **🤖 AI Agent Integration**: MCP-compatible interface for seamless AI agent interaction
- **📍 Location-aware**: Supports multiple locations with location-specific pricing models
- **⚡ Real-time**: Fast prediction responses for interactive applications
- **🔧 Extensible**: Easy to add new locations and retrain models

## Use Cases

- Real estate price estimation
- Property investment analysis
- Market research and analysis
- AI-powered real estate assistants
- Automated property valuation systems

## Technology Stack

- **Python 3.12+**: Core programming language
- **FastMCP**: Model Context Protocol server framework
- **NumPy**: Numerical computing for ML operations
- **Pickle**: Model serialization and storage
- **JSON**: Data configuration and location mappings

## Getting Started

For detailed setup instructions, API documentation, and usage examples, see the [main application README](price-prediction-agentic-ai/README.md).

## Development

### Prerequisites

- Python 3.12 or higher
- Virtual environment (recommended)
- Git for version control

### Setting up Development Environment

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate     # On Windows
   ```

2. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run tests to verify setup:
   ```bash
   python test_dependencies.py
   ```

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Add tests if applicable
5. Commit your changes (`git commit -m 'Add some feature'`)
6. Push to the branch (`git push origin feature/your-feature`)
7. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

- 📖 Documentation: Check the individual component READMEs
- 🐛 Issues: Report bugs via GitHub Issues
- 💬 Discussions: Use GitHub Discussions for questions and ideas

## Roadmap

- [ ] Add support for more property types
- [ ] Implement additional ML models for comparison
- [ ] Add web interface for direct user interaction
- [ ] Expand location coverage
- [ ] Add historical price trend analysis
- [ ] Implement model performance monitoring

---

For more detailed information about the MCP server implementation, please refer to the [price-prediction-agentic-ai README](price-prediction-agentic-ai/README.md).
