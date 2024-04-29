import React, { useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "codemirror/lib/codemirror.css";
import "codemirror/theme/dracula.css";
import "codemirror/mode/python/python.js";
import "codemirror/mode/clike/clike.js";
import "codemirror/mode/javascript/javascript.js";
import "codemirror/mode/clike/clike.js";
import "codemirror/addon/edit/closebrackets.js";
import { Controlled as CodeMirror } from "react-codemirror2";
import axios from "axios";

function Playground() {
  const [editorContent, setEditorContent] = useState("");
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");
  const [outputA, setOutputA] = useState("");
  const [geminiCode, setGeminiCode] = useState("");
  const [openAICode, setOpenAICode] = useState("");
  const [selectedLanguage, setSelectedLanguage] = useState("Python");
  const [isOutputEnabled, setIsOutputEnabled] = useState(false);
  const [chatMessages, setChatMessages] = useState([]); // State to store chat messages
  const [userInput, setUserInput] = useState(""); // State to store user input

  const handleLanguageChange = (e) => {
    setSelectedLanguage(e.target.value);
  };
  const handleRunGemini=async()=>{
    const code = {
        code: geminiCode,
        input: input,
        lang: selectedLanguage,
      };
      try {
        const response = await fetch("http://localhost:5000/compile", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(code),
      });

      const data = await response.json();
    //   setOutput(data)
      setOutput(data.output);
      } catch (error) {
        console.log(error.message)
      }
  }
  const handleRunOpenAi=async()=>{
    try {
        const codeA={
            code: openAICode,
              input: input,
              lang: selectedLanguage,
            }
            try {
                const responseA = await fetch("http://localhost:5000/compile", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(codeA),
      });

      const dataA = await responseA.json();
      setOutputA(dataA.output)
            } catch (error) {
                console.log(error.message)
            }
    } catch (error) {
        
    }
  }
  const handleRun = async () => {
    // Display user input as a chat message
    setChatMessages((prevMessages) => [
      ...prevMessages,
      { message: userInput, isUser: true },
    ]);
    setUserInput(""); // Clear the input field after sending

    try {
    //   setIsOutputEnabled(true); // Enable output textarea for input

      // Display backend response as a chat message
    //   setChatMessages((prevMessages) => [
    //     ...prevMessages,
    //     { message: data.output, isUser: false },
    //   ]);

      // Fetch and set Gemini code
      const geminiResponse = await axios.post(
        "http://127.0.0.1:8000/api/codegenerator/",
        { prompt: userInput, language: selectedLanguage }
      );
      setGeminiCode(geminiResponse.data.gemini);
      // setOpenAICode(geminiResponse.data.openai)
    } catch (error) {
      console.error("Error:", error);
    }
  };

  const handlePromptSend = async () => {
    setEditorContent(""); // Clear the editor content
    handleRun();
  };

  useEffect(() => {
  }, [userInput, selectedLanguage]);

  return (
    <div className="container mt-5">
      <div className="row">
        <div className="col-lg-6 mb-3">
          <label className="visually-hidden" htmlFor="inlineFormSelectPref">
            Language
          </label>
          <select
            className="form-select"
            id="inlineFormSelectPref"
            onChange={handleLanguageChange}
            value={selectedLanguage}
          >
            <option value="Java">Java</option>
            <option value="Cpp">Cpp</option>
            <option value="Python">Python</option>
            <option value="JavaScript">JavaScript</option>
            <option value="C">C</option>
          </select>
          <div className="d-flex justify-content-between bg-dark rounded p-2">
            <div className="d-flex justify-content-between align-items-center bg-dark rounded ">
              <div>
                <label className="text-light mb-0" htmlFor="geminiOutput">
                  Code   
                </label>
              </div>
              <div style={{margin:'auto'}}>
                <button
                  type="button"
                  
                  className="btn btn-success me-2"
                  onClick={handleRunOpenAi}
                >
                  Run <i className="bi bi-play-fill"></i>
                </button>
              </div>
            </div>
          </div>
          <div className="w-100">
            <CodeMirror
              value={openAICode}
              options={{
                mode:
                  selectedLanguage === "Python"
                    ? "text/x-python"
                    : selectedLanguage === "Java"
                    ? "text/x-java"
                    : selectedLanguage === "JavaScript"
                    ? "text/javascript"
                    : selectedLanguage === "C"
                    ? "text/x-csrc"
                    : "text/x-c++src",
                theme: "dracula",
                lineNumbers: true,
                autoCloseBrackets: true,
              }}
              onBeforeChange={(editor, data, value) => {
                setOpenAICode(value);
              }}
            />
          </div>
        </div>
        <div className="col-lg-6">
          <div className="bg-dark rounded p-4">
            {/* Display Gemini code */}
            <div className="d-flex justify-content-between align-items-center bg-dark rounded ">
              <div>
                <label className="text-light mb-0" htmlFor="geminiOutput">
                  Code
                </label>
              </div>
              <div>
                <button
                  type="button"
                  className="btn btn-success me-2"
                  onClick={handleRunGemini}
                >
                  Run <i className="bi bi-play-fill"></i>
                </button>
              </div>
            </div>
            <CodeMirror
              value={geminiCode}
              options={{
                mode:
                  selectedLanguage === "Python"
                    ? "text/x-python"
                    : selectedLanguage === "Java"
                    ? "text/x-java"
                    : selectedLanguage === "JavaScript"
                    ? "text/javascript"
                    : selectedLanguage === "C"
                    ? "text/x-csrc"
                    : "text/x-c++src",
                theme: "dracula",
                lineNumbers: true,
                autoCloseBrackets: true,
              }}
              onBeforeChange={(editor, data, value) => {
                setGeminiCode(value);
              }}
            />
          </div>
        </div>
        <div className="col-lg-6">
          <div className="bg-dark rounded p-4">
            {/* Display OpenAI code */}
            <label className="text-light mb-2" htmlFor="openAIOutput">
              Output
            </label>
            <textarea
              className="form-control"
              id="output"
              value={outputA}
              readOnly={!isOutputEnabled}
              onChange={(e) => setInput(e.target.value)}
            ></textarea>
          </div>
        </div>
        <div className="col-lg-6">
          <div className="bg-dark rounded p-4">
            {/* Display chat messages */}
            <label className="text-light mb-2" htmlFor="output">
              Output
            </label>
            <textarea
              className="form-control"
              id="output"
              value={output}
              readOnly={!isOutputEnabled}
              onChange={(e) => setInput(e.target.value)}
            ></textarea>
          </div>
        </div>
        {/* {chatMessages.map((chat, index) => (
          <div key={index} className={"user-message"}>
            {chat.message}
          </div>
        ))} */}
        <div className="mt-3">
          <input
            type="text"
            className="form-control"
            placeholder="Enter your prompt..."
            value={userInput}
            onChange={(e) => setUserInput(e.target.value)}
          />
          <button
            type="button"
            className="btn btn-primary mt-2"
            onClick={handlePromptSend}
          >
            Send Prompt
          </button>
          {geminiCode && (
        <div className="mt-3">
          <h3>Response:</h3>
          <pre>{geminiCode}</pre>
        </div>
      )}
        </div>
      </div>
    </div>
  );
}

export default Playground;