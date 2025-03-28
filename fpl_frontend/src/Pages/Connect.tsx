import { useNavigate } from 'react-router-dom';
import Navbar from '../Components/Navbar/Navbar';
import '../styles/Global.css';
import '../Components/Navbar/Navbar.css';
import '../styles/Connect.css';
import PlayerCard from '../Components/PlayerCard/PlayerCard';
import Button from '../Components/Button/Button';

const Connect = () => {
  const navigate = useNavigate();

  return (
    <div className="page-container">  {/* NEW container for the entire page */}
      <Navbar />
      
      {/* Main scrolling area */}
      <div className="connect-page">
        
        {/* Team Info (not fixed anymore, so remove position: fixed) */}
        <div className="team-info">
          <div className="team-name">Team Name</div>
          <div className="team-manager">Dylan Byrne</div>
          <div className="game-week">GW 20</div>
          <div className="points">Points: 54</div>
        </div>

        <section className="goalkeeper">
          <PlayerCard name="Goalkeeper" points={10} />
        </section>

        <section className="defenders">
          {[...Array(5)].map((_, i) => (
            <PlayerCard key={i} name={`Defenders ${i + 1}`} points={10} isViceCaptain = {i === 4} />
          ))}
        </section>

        <section className="midfielders">
          {[...Array(5)].map((_, i) => (
            <PlayerCard key={i} name={`Midfielders ${i + 1}`} points={8} isCaptain = {i === 4} />
          ))}
        </section>

        <section className="forwards">
          {[...Array(3)].map((_, i) => (
            <PlayerCard key={i} name={`Calvert-Lewin ${i + 1}`} points={12} showSubOn = {i === 0} />
          ))}
        </section>

        <section className="bench">
          {[...Array(5)].map((_, i) => (
            <PlayerCard
              key={i}
              name={`Substitution ${i + 1}`}
              points={3 + i}
              showSubOff = {i === 4}
            />
          ))}
        </section>

        {/* Buttons at the bottom of the main content flow, not fixed */}
        <div className="bottom-right-buttons">
          <Button 
            label="Confirm & Get Bet-Builder" 
            onClick={() => console.log('Confirm clicked')} 
            className="confirm-button" 
          />
          <Button 
            label="That's not my team" 
            onClick={() => navigate('/')} 
            className="cancel-button" 
          />
        </div>
      </div>
    </div>
  );
};

export default Connect;