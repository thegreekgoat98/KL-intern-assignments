import React, { useState } from "react";
import FormDataCard from "./FormDataCard";
import SearchBar from "./SearchBar";






const Register = () => {
  const [formData, setFormData] = useState({
    name: "",
    city: "",
    state: "",
    gender: "",
    phone: "",
  });

  const { name, city, state, gender, phone } = formData;

  const handleInputChange = (event) => {
    setFormData({
      ...formData,
      [event.target.name]: event.target.value,
    });
  };

  const [submittedData, setSubmittedData] = useState([]);
  const [searchQuery, setSearchQuery] = useState("");

  const handleSearch = (query) => {
    setSearchQuery(query);
  };


  const handleSubmit = (event) => {
    event.preventDefault();
    setSubmittedData([...submittedData, formData]);
    setFormData({
      name: "",
      city: "",
      state: "",
      gender: "",
      phone: "",
    });
  };

  

  return (
    <>
      <form className="register-form" onSubmit={handleSubmit}>
        <label className="register-label">
          Name:
          <input
            className="register-input"
            type="text"
            name="name"
            value={name}
            onChange={handleInputChange}
          />
        </label>
        <br />
        <label className="register-label">
          City:
          <input
            className="register-input"
            type="text"
            name="city"
            value={city}
            onChange={handleInputChange}
          />
        </label>
        <br />
        <label className="register-label">
          State:
          <input
            className="register-input"
            type="text"
            name="state"
            value={state}
            onChange={handleInputChange}
          />
        </label>
        <br />
        <label className="register-label">
          Gender:
          <input
            className="register-input"
            type="text"
            name="gender"
            value={gender}
            onChange={handleInputChange}
          />
        </label>
        <br />
        <label className="register-label">
          Phone:
          <input
            className="register-input"
            type="tel"
            name="phone"
            value={phone}
            onChange={handleInputChange}
          />
        </label>
        <br />
        <button className="register-button" type="submit">
          Submit
        </button>
      </form>

      <div>
        <div className="cards-container">
          {submittedData.map((data, index) => (
            <FormDataCard key={index} formData={data} />
          ))}
        </div>
      </div>
      <hr/>
      <div className="search">
        <SearchBar handleSearch={handleSearch} />

        {submittedData
          .filter((data) =>
            data.name.toLowerCase().includes(searchQuery.toLowerCase())
          )
          .map((data, index) => (
            <FormDataCard key={index} formData={data} />
          ))}
      </div>

      
    </>
  );
};



export default Register;
