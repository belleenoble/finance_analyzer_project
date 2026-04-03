//file upload logic for react frontend

// Import React hook to store data that changes (state) 

import {useState} from "react";

function UploadForm() {
    // state declaration to store the selected file
    const [file, setFile] = useState(null);

    // state declaration to store the response from the backend
    const [response, setResponse] = useState(null); //response -> variable, setResponse -> function to update response

    //will run when the use selects a file to upload
    const handleFileChange = (event) => {
        setFile(event.target.files[0]);     //event.target.files = list of selected files, [i] - index of file
    };

// will run when the user submits the form
const handleSubmit = async (event) => {
    event.preventDefault();    //prevent default form submission behavior

    // error handling: (if no file is selected
    if(!file) {
        alert("Please select a file first!");
        return;
    }

    // create a FormData object(class) to send the file to the backend
    const formData = new FormData(); 

    formData.append("file", file); //"file" must match backend parameter name

    try {

        //send POST request to FastAPI backend
        const res = await fetch ("http://localhost:8000/upload", {
            method: "POST",
            body: formData
        });
        
        //convert reponse to JSON and then store it in state
        const data = await res.json();
        setResponse(data); //updating state with backend response

        // error handling
    } catch (error) {
        console.error("Error uploading file:", error);
    }
};

return (
    <div>
        <h2> Upload your Financial Data!</h2>
        {/*
        File Input and Submit Button for handleSubmit function
        */}
        <form onSubmit={handleSubmit}> {/* when user submits a form -> run handleSubmit */}
            <input type="file" accept =".csv" onChange={handleFileChange} />
            <button type="submit">Upload</button>
        </form>

        {/* Only show this if response exists */}
        {response && (
            <div>
            <h3>Backend Response</h3>

            {/* Pretty print JSON */}
            <pre>{JSON.stringify(response, null, 2)}</pre>
            </div>
        )}
        </div>
    );
}

export default UploadForm;