import { Link } from 'react-router-dom' 
import './NotFoundPage.css'

const NotFoundPage = () => {
    return (
    <div> 
        <h1>Not Found - 404</h1> 
        <Link to="/">Go to Home</Link>
    </div>
    )
}

export default NotFoundPage