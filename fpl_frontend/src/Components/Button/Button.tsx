import './Button.css';

interface ButtonProps {
  label: string;
  onClick: (e: React.MouseEvent | React.FormEvent) => void;
  type?: 'button' | 'submit'; // Allows both default and form-submit buttons
  className?: string; // Optional for extra styles
}

const Button: React.FC<ButtonProps> = ({ label, onClick, type = 'button', className = '' }) => {
  return (
    <button className={`custom-button ${className}`} type={type} onClick={onClick}>
      {label}
    </button>
  );
};

export default Button;