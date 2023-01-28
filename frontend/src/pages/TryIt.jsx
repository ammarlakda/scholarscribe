import React from "react";
import { useState } from "react";
import "../../styles/pages/tryit.scss";
import Button from "../components/Button";
import Layout from "../components/Layout";
import { QueryClient, QueryClientProvider, useQuery } from "react-query";
import Response from "../components/Response";

const queryClient = new QueryClient();

const TryIt = () => {
  const [statusText, setStatusText] = useState("");
  const [selectedFile, setSelectedFile] = useState(null);
  const [validToSub, setValidToSub] = useState(false);
  const [fetchInit, setFetchInit] = useState(false);

  async function fetchData() {
    const formData = new FormData();

    formData.append("file", selectedFile);

    const req = await fetch(`${import.meta.env.VITE_API_URL}/`, {
      method: "POST",
      body: formData,
    });

    const res = await req.text();
    return res;
  }

  const getFileUploadHandler = (e) => {
    const file = e.target.files[0];
    if (file.name.endsWith(".mp4") || file.name.endsWith(".mp3")) {
      setSelectedFile(file);
      setValidToSub(true);
      setStatusText(file.name);
    } else {
      setStatusText("File is not of type mp3 or mp4");
      setValidToSub(false);
      setSelectedFile(null);
    }
  };

  const handleSubmission = () => {
    setFetchInit(false);
    setFetchInit(true);
  };

  const clearFile = () => {
    setValidToSub(false);
    setStatusText("");
    setSelectedFile(null);
    queryClient.cancelQueries({ queryKey: ["res"] });
    setFetchInit(false);
  };

  return (
    <Layout>
      <div className="tryit">
        <h2>Upload an MP3 or MP4 File</h2>
        <input type="file" id="upload" onChange={getFileUploadHandler} />
        <Button styling="tryit__upload-button">
          <label htmlFor="upload">Upload</label>
        </Button>
        {statusText && (
          <>
            <div className="tryit__status-text">{statusText}</div>
            {!!selectedFile && (
              <Button styling="tryit__clear" onClick={clearFile}>
                X
              </Button>
            )}
          </>
        )}
        <Button
          onClick={handleSubmission}
          disabled={!validToSub}
          styling="tryit__submit"
        >
          Submit
        </Button>
        <QueryClientProvider client={queryClient}>
          {fetchInit && <Response fetchData={fetchData} />}
        </QueryClientProvider>
      </div>
    </Layout>
  );
};

export default TryIt;
