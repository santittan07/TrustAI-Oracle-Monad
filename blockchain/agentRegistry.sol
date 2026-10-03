// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract AgentRegistry {

    // 1. Estructura que guarda la información de cada Bot de IA en la blockchain
    struct AIAgent {
        address creator;          // Billetera del desarrollador dueño del bot
        string ipfsMetadata;      // Link (IPFS) con el nombre, descripción y foto del bot
        uint256 totalOperations;  // Cantidad de tareas o transacciones financieras auditadas
        uint256 positiveFeedback; // Votos de confianza acumulados
        uint256 negativeFeedback; // Votos de penalización por fallas o errores
        bool isRegistered;        // Control para saber si el bot existe
    }

    // 2. Mapeo principal (funciona como tu tabla de Base de Datos)
    // ID único del Bot (bytes32) => Estructura con sus datos
    mapping(bytes32 => AIAgent) public agents;

    // 3. Mapeo de control para que un usuario no vote dos veces al mismo bot
    // ID del Bot => (Billetera del Usuario => Ya Votó?)
    mapping(bytes32 => mapping(address => bool)) public hasVoted;

    // 4. Eventos para que la página web de tu amigo escuche los cambios en tiempo real
    event AgentCreated(bytes32 indexed agentId, address indexed creator, string metadata);
    event FeedbackSubmitted(bytes32 indexed agentId, address indexed voter, bool isPositive, uint256 newScore);

    /**
     * @notice Registra un nuevo bot de IA en el sistema de reputación.
     * @param _salt Una palabra clave aleatoria para garantizar un ID único.
     * @param _metadata El link descentralizado con la información visual del bot.
     */
    function registerAgent(string calldata _salt, string calldata _metadata) external returns (bytes32) {
        // Generamos un hash de 32 bytes único combinando el texto, la billetera y el tiempo actual
        bytes32 agentId = keccak256(abi.encodePacked(_salt, msg.sender, block.timestamp));
        require(!agents[agentId].isRegistered, "El agente ya existe");

        agents[agentId] = AIAgent({
            creator: msg.sender,
            ipfsMetadata: _metadata,
            totalOperations: 0,
            positiveFeedback: 0,
            negativeFeedback: 0,
            isRegistered: true
        });

        emit AgentCreated(agentId, msg.sender, _metadata);
        return agentId;
    }

    /**
     * @notice Permite a los usuarios o protocolos calificar el comportamiento de un bot.
     * @param _agentId El ID único del bot que se va a calificar.
     * @param _approved True si el bot operó bien, False si falló o generó pérdidas.
     */
    function submitVote(bytes32 _agentId, bool _approved) external {
        require(agents[_agentId].isRegistered, "El agente no existe");
        require(!hasVoted[_agentId][msg.sender], "Ya calificaste a este agente");

        AIAgent storage agent = agents[_agentId];
        agent.totalOperations += 1;

        if (_approved) {
            agent.positiveFeedback += 1;
        } else {
            agent.negativeFeedback += 1;
        }

        hasVoted[_agentId][msg.sender] = true;

        // Calculamos el score actual y emitimos el aviso al frontend
        uint256 currentScore = calculateScore(_agentId);
        emit FeedbackSubmitted(_agentId, msg.sender, _approved, currentScore);
    }

    /**
     * @notice Función de lectura gratuita que calcula el porcentaje de éxito del bot (0 a 100).
     */
    function calculateScore(bytes32 _agentId) public view returns (uint256) {
        AIAgent memory agent = agents[_agentId];
        if (agent.totalOperations == 0) return 0;
        return (agent.positiveFeedback * 100) / agent.totalOperations;
    }
}