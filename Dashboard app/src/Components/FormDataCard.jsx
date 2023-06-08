import React, { useState } from "react";

const FormDataCard = ({ formData }) => {
  const [showDetails, setShowDetails] = useState(false);

  const toggleDetails = () => {
    setShowDetails(!showDetails);
  };

  return (
    <div className="form-data-card" onClick={toggleDetails}>
      <h3>{formData.name}</h3>
      <p>Phone: {formData.phone}</p>
      {showDetails && (
        <div className="card-details">
          <p>City: {formData.city}</p>
          <p>State: {formData.state}</p>
          <p>Gender: {formData.gender}</p>
        </div>
      )}
    </div>
  );
};

export default FormDataCard;
