# Multi Agent AI System for Stock Research

A sophisticated multi-agent AI system designed for comprehensive stock research and analysis using the Agno framework.

## 🚀 Features

- **Web Research Agent**: Searches the internet for real-time stock information
- **Finance Agent**: Retrieves detailed financial data from Yahoo Finance
- **Team Coordination**: Multi-agent system that coordinates research and analysis
- **Real-time Data**: Live stock prices, financial metrics, and market analysis
- **Comprehensive Reports**: Detailed analysis with tables and markdown formatting

## 🛠️ Technology Stack

- **Agno**: Multi-agent AI framework
- **Groq**: LLM provider (Llama 3.3 70B model)
- **DuckDuckGo**: Web search capabilities
- **YFinance**: Financial data provider
- **Python**: Core programming language

## 📋 Prerequisites

- Python 3.8+
- Groq API key
- Internet connection for real-time data

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd "Multi Agent AI system for Stock Research"
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**:
   ```bash
   # Windows
   .\venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## 🔧 Configuration

### Getting a Groq API Key

1. Visit [https://console.groq.com/](https://console.groq.com/)
2. Sign up or log in to your account
3. Generate a new API key
4. Add the key to your `.env` file

## 🎯 Usage

Run the main application:

```bash
python main.py
```

The system will:
1. Initialize the web research agent
2. Initialize the finance agent
3. Create a team of agents
4. Process stock research queries
5. Provide comprehensive analysis

## 📁 Project Structure

```
Multi Agent AI system for Stock Research/
├── main.py              # Main application file
├── requirements.txt      # Python dependencies
├── .env                 # Environment variables (not tracked)
├── .gitignore          # Git ignore rules
├── README.md           # Project documentation
├── test_api.py         # API key testing script
└── venv/               # Virtual environment (not tracked)
```

## 🤖 Agent Architecture

### Web Agent
- **Purpose**: Internet research and information gathering
- **Tools**: DuckDuckGo search
- **Capabilities**: Web scraping, news analysis, market sentiment

### Finance Agent
- **Purpose**: Financial data analysis
- **Tools**: YFinance integration
- **Capabilities**: Stock prices, financial metrics, company information

### Team Agent
- **Purpose**: Coordination and synthesis
- **Role**: Orchestrates multiple agents for comprehensive analysis
- **Output**: Structured reports with tables and markdown

## 🔍 Example Queries

- "What is the latest financial data for Tesla?"
- "Analyze the current market position of Apple"
- "Get comprehensive data for Tata Motors stock"

## 📊 Output Format

The system provides:
- Real-time stock prices
- Financial metrics and ratios
- Company information
- Market analysis
- Web-sourced insights
- Structured tables and reports

## 🔒 Security

- API keys are stored in `.env` file (not tracked by git)
- Sensitive data is excluded from version control
- Virtual environment is not committed

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Troubleshooting

### Common Issues

1. **API Key Error**: Ensure your Groq API key is valid and properly set in `.env`
2. **Import Errors**: Make sure all dependencies are installed
3. **Network Issues**: Check your internet connection for web searches

### Testing API Key

Use the test script to verify your API key:

```bash
python test_api.py
```

## 📞 Support

For issues and questions, please open an issue in the repository. 