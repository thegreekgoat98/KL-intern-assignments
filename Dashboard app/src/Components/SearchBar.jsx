import React from "react";

const SearchBar = ({ handleSearch }) => {
  return (
    <>
    <label htmlFor="search-input"><h1>Search by names:</h1></label>
    <br />
    <input
      className="search-input"
      type="text"
      placeholder="Search by name"
      onChange={(e) => handleSearch(e.target.value)}
    />
    </>
  );
};

export default SearchBar;
