import React, { useEffect, useRef } from "react";
import ace from "ace-builds"; 
import "ace-builds/src-noconflict/theme-cobalt"; 
import "ace-builds/src-noconflict/mode-javascript"; 
import './style.css'
const Ace = () => {
  const editorRef = useRef(null);
  useEffect(() => {
    const editor = ace.edit(editorRef.current);
    editor.setTheme("ace/theme/cobalt");
    editor.session.setMode("ace/mode/javascript");
    editor.session.on("change", function () {
      console.log("Editor content changed");
    });
    return () => {
      editor.destroy();
    };
  }, []);

  return (
    <>
    <div className="editor-container">
      <div id="editor" ref={editorRef}></div>
    </div>
    </>
  );
};

export default Ace;
