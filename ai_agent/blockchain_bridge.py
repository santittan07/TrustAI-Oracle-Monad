import json

# ==========================================================
# PUNTO DE INTEGRACIÓN: ABI ACTUALIZADO DEL INTEGRANTE A ✅
# ==========================================================
CONTRACT_ADDRESS = "0xd9145CCE52D386f254917e481eB44e9943F39138"

CONTRACT_ABI = [
	{
		"anonymous": False,
		"inputs": [
			{"indexed": True, "internalType": "bytes32", "name": "agentId", "type": "bytes32"},
			{"indexed": True, "internalType": "address", "name": "creator", "type": "address"},
			{"indexed": False, "internalType": "string", "name": "metadata", "type": "string"}
		],
		"name": "AgentCreated",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{"indexed": True, "internalType": "bytes32", "name": "agentId", "type": "bytes32"},
			{"indexed": True, "internalType": "address", "name": "voter", "type": "address"},
			{"indexed": False, "internalType": "bool", "name": "isPositive", "type": "bool"},
			{"indexed": False, "internalType": "uint256", "name": "newScore", "type": "uint256"}
		],
		"name": "FeedbackSubmitted",
		"type": "event"
	},
	{
		"inputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
		"name": "agents",
		"outputs": [
			{"internalType": "address", "name": "creator", "type": "address"},
			{"internalType": "string", "name": "ipfsMetadata", "type": "string"},
			{"internalType": "uint256", "name": "totalOperations", "type": "uint256"},
			{"internalType": "uint256", "name": "positiveFeedback", "type": "uint256"},
			{"internalType": "uint256", "name": "negativeFeedback", "type": "uint256"},
			{"internalType": "bool", "name": "isRegistered", "type": "bool"}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [{"internalType": "bytes32", "name": "_agentId", "type": "bytes32"}],
		"name": "calculateScore",
		"outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{"internalType": "bytes32", "name": "", "type": "bytes32"},
			{"internalType": "address", "name": "", "type": "address"}
		],
		"name": "hasVoted",
		"outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{"internalType": "string", "name": "_salt", "type": "string"},
			{"internalType": "string", "name": "_metadata", "type": "string"}
		],
		"name": "registerAgent",
		"outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
		"stateMutability": "external",
		"type": "function"
	},
	{
		"inputs": [
			{"internalType": "bytes32", "name": "_agentId", "type": "bytes32"},
			{"internalType": "bool", "name": "_approved", "type": "bool"}
		],
		"name": "submitVote",
		"outputs": [],
		"stateMutability": "external",
		"type": "function"
	}
]

def get_onchain_agents():
    """
    Retorna la lista de agentes para el Frontend de app.py.
    """
    return [
        {
            "id": "0x1a7f72...892b", 
            "name": "Alpha-DeFi-Trader", 
            "description": "Bot autónomo de arbitraje en pools de liquidez.", 
            "tasks": 142, 
            "reputation": 95
        },
        {
            "id": "0x2b3c54...456d", 
            "name": "Sentinel-Risk-Auditor", 
            "description": "Monitorea vulnerabilidades en Smart Contracts las 24 horas.", 
            "tasks": 68, 
            "reputation": 82
        },
        {
            "id": "0x3c9e11...710f", 
            "name": "Predictor-Max-Mev", 
            "description": "Agente avanzado enfocado en capturar valor MEV en Monad.", 
            "tasks": 110, 
            "reputation": 45
        }
    ]

def register_agent_onchain(name, description, user_private_key):
    return True
