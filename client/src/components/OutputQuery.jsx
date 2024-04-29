// import React from "react";
// import utilsContext from "../context/utilsContext";

// export default function OutputQuery() {
//     const [sidebarData, setSidebarData, mainContentInput, setMainContentInput, queryResponse, setQueryResponse] = React.useContext(utilsContext);   //Global Context

//     // Function to handle test query click
//     const handleTestQueryClick = () => {
//         // Logic to handle the test query action
//         console.log("Test query clicked");
//     };

//     return (
//         <div className="output-query-container">
//             <h2>Query Output:</h2>
//             <div className="query-and-button-container">
//                 <div className="query-container">
//                     <p className="result-query">{queryResponse.response[0]}</p>
//                 </div>
//                 <button className="test-query-button" onClick={handleTestQueryClick}>
//                     Copy Output
//                 </button>
//             </div>
//         </div>
//     );
// }
import React, { useEffect, useRef } from "react";
import { Controlled as CodeMirror } from "react-codemirror2";
import "codemirror/lib/codemirror.css";
import "codemirror/mode/sql/sql";
import utilsContext from "../context/utilsContext";
import "codemirror/theme/dracula.css";
export default function OutputQuery() {
    const [sidebarData, setSidebarData, mainContentInput, setMainContentInput, queryResponse, setQueryResponse] = React.useContext(utilsContext);   //Global Context
    const queryContainerRef = useRef(null);

    // Function to handle test query click
    const handleCopyOutput = () => {
        if (queryContainerRef.current) {
            const queryText = queryContainerRef.current.editor.getValue();
            navigator.clipboard.writeText(queryText).then(() => {
                console.log("Output copied successfully!");
            }).catch((error) => {
                console.error("Failed to copy output:", error);
            });
        }
    };

    return (
        <div className="output-query-container">
            <h2>Query Output:</h2>
            <div className="query-and-button-container">
                <div className="query-container">
                    <CodeMirror
                        value={queryResponse}
                        options={{
                            mode: "JavaScript",
                            theme: "dracula",
                            lineNumbers: true,
                            readOnly: true,
                        }}
                        editorDidMount={(editor) => {
                            queryContainerRef.current = editor;
                        }}
                    />
                </div>
            </div>
        </div>
    );
}
