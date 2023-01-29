import React from "react";
import Button from "./Button";
import "../../styles/components/dashboard.scss";

const DashboardComponent = ({
  getFileUploadHandler,
  statusText,
  selectedFile,
  clearFile,
  handleSubmission,
  validToSub,
}) => {
  return (
    <div className="dashboard">
      <h2>Upload an MP3 or MP4 File</h2>
      <input type="file" id="upload" onChange={getFileUploadHandler} />
      <Button styling="dashboard__upload-button">
        <label htmlFor="upload">Upload</label>
      </Button>
      {statusText && (
        <div>
          <div className="dashboard__status-text">{statusText}</div>
          {!!selectedFile && (
            <Button styling="dashboard__clear" onClick={clearFile}>
              X
            </Button>
          )}
        </div>
      )}
      <Button
        onClick={handleSubmission}
        disabled={!validToSub}
        styling="dashboard__submit"
      >
        Submit
      </Button>
    </div>
  );
};

export default DashboardComponent;
