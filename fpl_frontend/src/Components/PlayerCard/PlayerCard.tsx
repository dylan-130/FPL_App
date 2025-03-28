import './PlayerCard.css';

interface PlayerCardProps {
    name: string;
    points: number;
    isCaptain?: boolean;
    isViceCaptain?: boolean;
    showSubOn?: boolean;
    showSubOff?: boolean;
}

const PlayerCard: React.FC<PlayerCardProps> = ({ 
  name, 
  points, 
  isCaptain = false, 
  isViceCaptain = false,
  showSubOn = false, 
  showSubOff = false,
 }) => {
  return (
    <div className="player-card">
      <div className="circle-icon"></div>
      <div className="player-icons">
        {isCaptain && <span className="captain-icon">C</span>}
        {isViceCaptain && <span className="vice-captain-icon">V</span>}
      </div>
      <p>{name}</p>
      <p>{points}</p>
      <div className="sub-icons">
      {showSubOn && <span className="sub-on-icon">⃕</span>}
      {showSubOff && <span className="sub-off-icon">⃔</span>}
    </div>
    </div>
  );
};

export default PlayerCard;