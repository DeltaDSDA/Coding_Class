import React from 'react';

const TextItem = ({ text, id, handleClick }) => {
	return (
		<div>
			<p> { text } </p>
			<button onClick={() => handleClick(id)}> Delete </button>
		</div>
	);
};

export default TextItem;
