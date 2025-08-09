# Price Prediction Agentic AI

A machine learning-powered house price prediction service built with MCP (Model Context Protocol) server architecture. This project provides real-time house price predictions based on location, number of bedrooms, bathrooms, and area.

## Features

- **Real-time Price Prediction**: Get instant house price estimates based on property features
- **MCP Server Integration**: Built using FastMCP for seamless integration with AI agents
- **Location-based Pricing**: Supports location-specific price modeling
- **RESTful API**: Easy-to-use API endpoints for price predictions

## Project Structure

```
price-prediction-agentic-ai/
├── main.py                 # MCP server implementation
├── model/                  # Machine learning models and data
│   ├── dwelling_model.pickle  # Trained price prediction model
│   └── locations.json      # Location data and mappings
├── pyproject.toml          # Project configuration
├── uv.lock                 # Dependency lock file
└── README.md              # This file
```

## Installation

### Prerequisites

- Python 3.12 or higher
- uv package manager (recommended) or pip

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd price-prediction-chatbot
```

2. Install dependencies using uv (recommended):
```bash
cd price-prediction-agentic-ai
uv sync
```

Or using pip:
```bash
pip install -r ../requirements.txt
```

3. Activate the virtual environment:
```bash
# If using uv
uv shell

# If using venv
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate     # On Windows
```

## Usage

### Starting the MCP Server

```bash
python main.py
```

The server will start and load the machine learning model automatically.

### Available Tools

#### 1. House Price Prediction

Predict house prices based on property characteristics:

```python
housePrice(location: str, bedrooms: int, bathrooms: int, area: int) -> float
```

**Parameters:**
- `location`: Property location (e.g., "anekal")
- `bedrooms`: Number of bedrooms
- `bathrooms`: Number of bathrooms
- `area`: Property area in square feet

**Returns:** Predicted price as a float

#### 2. Sum Tool (Example)

A simple addition tool for demonstration:

```python
sum(a: int, b: int) -> int
```

### Resources

#### Greeting Resource

Access personalized greetings via the resource endpoint:

```
greeting://{name}
```

## Model Information

The price prediction model is a trained machine learning model stored as a pickle file. It uses the following features:

- Property area (square feet)
- Number of bathrooms
- Number of bedrooms
- Location (one-hot encoded)

## Development

### Project Dependencies

- **numpy**: Numerical computing library for model operations
- **fastmcp**: MCP server framework
- **pickle**: Model serialization (built-in)
- **json**: Data handling (built-in)

### Adding New Locations

To add support for new locations:

1. Update the `locations.json` file in the `model/` directory
2. Retrain the model with new location data
3. Update the model pickle file

### Model Retraining

To retrain the model with new data:

1. Prepare your training data with the same feature structure
2. Train your model using your preferred ML framework
3. Save the model as `dwelling_model.pickle`
4. Update location mappings in `locations.json`

## API Integration

This MCP server can be integrated with various AI agents and applications that support the Model Context Protocol. The server provides tools that can be called by AI agents to get real-time price predictions.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions or issues, please open an issue on the GitHub repository.