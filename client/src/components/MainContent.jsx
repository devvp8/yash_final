import React from "react";
import InputTables from "./InputTables";
import OutputQuery from "./OutputQuery";

import utilsContext from "../context/utilsContext";
import QueryGenerator from "../pages/QueryGenerator";

export default function MainContent()
{
    const [sidebarData, setSidebarData, mainContentInput, setMainContentInput, queryResponse, setQueryResponse] = React.useContext(utilsContext);   //Global Context

    return (
        <div className="app">
            <header className="header">
                <h1>Query Generator</h1>
            </header>
            <main className="main-content">
            <h2>How can I help you today?</h2>
            <div className="card-container">
                <div className="card brainstorm">
                    <h3>Brainstorm content ideas</h3>
                    <p>
                        Generate content ideas for various media, including blog posts, articles, social media captions, email newsletters, and more.
                    </p>
                </div>
                <div className="card write-email">
                    <h3>Write an email</h3>
                    <p>
                        Craft compelling emails for different purposes, such as requesting a quote, pitching a product, or following up with a lead.
                    </p>
                </div>
                <div className="card explain-concept">
                    <h3>Explain a concept</h3>
                    <p>
                        Break down complex topics into easy-to-understand explanations, suitable for both adults and children.
                    </p>
                </div>
                    <div className="card more-options">
                    <h3>More options</h3>
                    <p>
                        Explore Codex's other capabilities, including writing different kinds of creative content, translating languages, and answering your questions in an informative way.
                    </p>
                </div>
            </div>
            {queryResponse ? <OutputQuery /> : null}
            <div className="chat-container">
                <h2>Ask your Query here: </h2>
                <input type="text" value={mainContentInput} onChange={(e) => setMainContentInput(e.target.value)} className="chat-input" placeholder="Your Query goes here!" />
            </div>
            </main>
        </div>
    );
}