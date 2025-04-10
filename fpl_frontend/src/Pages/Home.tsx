import { useRef } from 'react';
import { Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import '../styles/Global.css';
import '../Components/Navbar/Navbar.css';
import '../styles/Home.css';
import '../styles/SignIn.css';
import Button from '../Components/Button/Button';

function App() {
  const signInRef = useRef<HTMLDivElement>(null);
  const landingRef = useRef<HTMLDivElement>(null);
  const navigate = useNavigate();

  // Smooth scroll to sign-in
  const scrollToSignIn = () => {
    signInRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

// Navigate to Connect page and connect to backend API
const handleConnect = async (e: React.FormEvent) => {
  e.preventDefault();

  const teamName = (document.getElementById('teamName') as HTMLInputElement)?.value;
  const fullName = (document.getElementById('fullName') as HTMLInputElement)?.value;

  // Fetch from API
  try {
    const response = await fetch(`http://127.0.0.1:8000/api/get_player_id/?playerName=${fullName}&teamName=${teamName}`);
    const data = await response.json();

    console.log("Received from Django:", data);

    // You can handle the data here as needed, for example, storing it in a state or localStorage

    // Navigate to the next page only if fetch was successful
    navigate('/connect');
  } catch (err) {
    console.error("API error:", err);
  }
};

  return (
    <>
      {/* NAVBAR (fixed at top) */}
      <nav className="navbar">
        <div className="navbar-logo">FPL Pulse</div>
        <div className="navbar-links">
          <Link to='/'>Home</Link>
          <a onClick={scrollToSignIn}>Connect</a>
        </div>
      </nav>

      {/* HERO SECTION: full screen, out of the normal doc flow below the fixed nav */}
      <section ref={landingRef} className="hero-container">
        <div className="hero-content">
          <p className="hero-subtitle">It's almost time</p>
          <h1 className="hero-title">FPL Betting, Re‑Imagined!</h1>
          <Button 
            label="Get Started" 
            onClick={scrollToSignIn} 
            className="hero-button" 
        />
        </div>
      </section>

      {/* SIGN-IN SECTION: also full screen, visually below hero */}
      <section ref={signInRef} className="sign-in-section">
        <h2>Connect your Fantasy Premier League team!</h2>
        <form onSubmit={handleConnect}>
          <div>
            <label htmlFor="teamName">Team name *</label>
            <input
              id="teamName"
              type="text"
              placeholder="Enter your team name"
            />
          </div>
          <div>
            <label htmlFor="fullName">Your full name *</label>
            <input
              id="fullName"
              type="text"
              placeholder="Enter your full name"
            />
          </div>
          <Button 
            label="Connect" 
            onClick={handleConnect} 
            type="submit" 
            className="connect-button" 
        />
        </form>
      </section>
    </>
  );
}

export default App;