import React from "react"
import { Link, NavLink } from "react-router-dom"

export default function Header() {
    const activeStyles = {
        fontWeight: "bold",
        textDecoration: "underline",
        color: "#f8f8f8"
    }
    
    return (
        <header>
            <Link className="site-logo" to="/">#Codex</Link>
            <nav>
                <NavLink 
                    to="query-generator"
                    style={({isActive}) => isActive ? activeStyles : null}
                >
                    Query Generator
                </NavLink>
                <NavLink 
                    to="/code-generator"
                    style={({isActive}) => isActive ? activeStyles : null}
                >
                    Code Generator
                </NavLink>
                <NavLink 
                    to="vans"
                    style={({isActive}) => isActive ? activeStyles : null}
                >
                    Vans
                </NavLink>
                {/* <Link to="login" className="login-link">
                    <img 
                        src="../assets/images/avatar-icon.png" 
                        className="login-icon"
                    />
                </Link> */}
            </nav>
        </header>
    )
}