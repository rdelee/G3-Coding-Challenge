import React, { useState } from 'react'

const Login = (props) => {

    const[username, setUsername] = useState("");
    const[password, setPassword] = useState("");

    function handleSubmit(event) {
        event.preventDefault();
        let user = {
            "username": username,
            "password": password
        }
        console.log(user);
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label>Username: <p></p>
                    <input type="text" value={username} onChange={e => setUsername(e.target.value)} placeholder="please input username"/>
                </label>
                <p></p>
                <label>Password: <p></p>
                    <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="please input password"/>
                </label>
                <p></p>
                <input type="submit" value="Login!"/>
            </form>
        </div>
    )
}

export default Login;