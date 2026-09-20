import { getUser } from "../utils/Helper";
import { useNavigate } from "react-router";

const Home = () => {
    const navigate = useNavigate();

    const logout = () => {
        localStorage.removeItem("token");
        navigate("/");
    };

    return (
        <div>
            <h1>Home Page, Hi, {getUser().username}</h1>

            <button onClick={logout}>
                Logout
            </button>
        </div>
    );
};

export default Home;
