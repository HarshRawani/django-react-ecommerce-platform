import { Navigate } from "react-router"
import { isAuthenticated } from "./Helper"

const ProtectedRoute=({element})=>{
    return isAuthenticated()?element:<Navigate to="/"/>
}
export default ProtectedRoute