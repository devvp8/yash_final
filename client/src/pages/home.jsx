import React from "react"
import { useNavigate} from 'react-router-dom';


export default function Home(){

const navigate = useNavigate();
    return(
        <div className="home-container">
            <table>
                <tr>
                    <td>
      <div className="text-container">
        <p className="main-heading">Introducing the CodeGenerator</p>
        <p className="sub-heading">One Solution to Solve Problems and</p>
        <p className="sub-heading">Generate Code</p>
      </div>
      <div className="buttons-container">
        <button className="primary-button" onClick={() => navigate("/code-generator")}>Generate Codes</button>
        {/* <button className="secondary-button" onClick={() => navigate("/query-generator")}>Generate Query</button> */}
      </div></td>
      <td>
      <div className="image-container">
        <img src="https://miro.medium.com/v2/resize:fit:12000/0*tQQ7SLPOJfxaG4ZY" alt="CodeGenerator" className="home-image"/>
      </div>
      </td>
      </tr>
      </table>
    </div>
    );
}