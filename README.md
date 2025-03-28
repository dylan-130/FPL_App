# FPL Web App

## Overview
This repository hosts the ongoing development of a **Fantasy Premier League (FPL) web application**. The primary goal of this project is to provide users with a **seamless and dynamic experience** by leveraging advanced backend architecture and real-time data from the **FPL API** and **AWS**.

## Key Features
- **Dynamic User Input System**: Users input their **team name and full name** directly on the homepage. These inputs are used to dynamically query relevant data from the backend.
- **Proprietary API**: Built using **AWS**, this custom API points to a **Lambda function** that queries an **internal database** to retrieve a **unique player ID** based on user-provided information. This player ID is then used to fetch team-specific data from the **FPL API**.
- **Sophisticated Backend**: The application integrates **multiple layers of logic** to ensure accurate retrieval of player-specific data, without relying on dropdown menus or static lists.
- **AWS Integration**: Utilizes **AWS Lambda** for efficient, serverless computations, ensuring **scalability** and **reduced latency** when querying databases and APIs.

## Current State
The project is actively under development, with features being iteratively added and refined. The current focus is on:

- Perfecting the **dynamic querying mechanism** for retrieving accurate player data.
- Enhancing the **backend architecture** to handle high volumes of concurrent requests.
- Establishing a **seamless user experience** for entering data and retrieving personalized FPL insights.

## Future Potential
The long-term vision for this project extends beyond its current scope. Future iterations aim to transform this web application into a **fully-fledged platform** that generates bet-builder combinations based on user-specific FPL data. This will involve:

- **Advanced Data Analytics**: Using **machine learning algorithms** to analyze user FPL data and suggest optimal betting combinations.
- **User-Centric Features**: Providing **detailed insights** and recommendations tailored to individual users.
- **Scalable Architecture**: Expanding the backend to handle **complex computations** and **large-scale data integrations**.

## Technology Stack
- **Frontend**:  
  - **React** with **Vite** for a fast and optimized development experience.  
  - **TypeScript** for type safety and better maintainability.  

- **Backend**:  
  - **Django** (Python) for API development and data handling.  
  - **JavaScript** for backend scripting where needed.  

- **API Integration**:  
  - Seamless integration with the **FPL API** to fetch real-time player and team data.  

- **Database**:  
  - Proprietary **internal database** designed to store and manage user inputs and corresponding player IDs.  

- **Cloud Services**:  
  - **AWS Lambda** for serverless execution, ensuring scalability and cost efficiency.  

## How It Works
1. **User Input**: Users enter their **team name** and **full name** on the homepage.
2. **Backend Query**: The **proprietary API**, powered by **AWS Lambda**, retrieves the **unique player ID** corresponding to the inputted details by querying the internal database.
3. **FPL API Call**: The retrieved **player ID** is used to dynamically fetch **user-specific FPL data** from the **FPL API**.
4. **Data Display**: The application renders the fetched data **in real-time**, providing users with actionable insights into their FPL teams.

## Contributions
This project is actively being developed and is **not currently open to external contributions**. For inquiries, feel free to contact the repository owner.

## Contact
For more information or collaboration opportunities, please reach out to **Dylan Byrne** at **dylan8byrne@gmail.com**.

---

Stay tuned for further updates as this project evolves into a **comprehensive platform** for both FPL enthusiasts and betting aficionados.
---
