import React from "react";

export default function InputTables()
{
    let inputTableArray = [   //get response array from backend
        {
            key: 1,
            tableName: "Brainstorm content ideas",
            tableContent: "Generate content ideas for various media, including blog posts, articles, social media captions, email newsletters, and more."
        },
        {
            key: 2,
            tableName: "Write an email",
            tableContent: "Craft compelling emails for different purposes, such as requesting a quote, pitching a product, or following up with a lead."
        },
        {
            key: 3,
            tableName: "Explain a concept",
            tableContent: "Break down complex topics into easy-to-understand explanations, suitable for both adults and children."
        }
    ];

    let inputTableElements = inputTableArray.map((object) => {
        return (
            <div className="card" key={object.key}>
                <h3>{object.tableName}</h3>
                <p>{object.tableContent}</p>
            </div>
        );
    });

    return (
        <>
            {inputTableElements}
        </>
    );
}