import { Link } from 'react-router-dom' 
import './Home.css'

const HomePage = () => {
    return (
    <div> 
        <h1>Home Page</h1> 
        <Link to="/About">Go to Home</Link>
    </div>
    )
}

export default HomePage