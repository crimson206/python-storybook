import React from 'react';

// JSON 데이터를 파라미터로 받는 컴포넌트
const PrettyJsonDisplay = ({ data }) => {
  // 'story name'을 생성
  const storyName = `${data.title} / ${data.name}`;

  return (
    <div style={{ margin: '20px', padding: '20px', border: '1px solid #ccc', borderRadius: '8px' }}>
      <h2>Story Name: {storyName}</h2>
      <h3>Render Name: {data.render_name}</h3>
      {data.docs && <div><strong>Docs:</strong> {data.docs}</div>}
      {!data.docs && <div><strong>Docs:</strong> No documentation provided.</div>}
      <div><strong>Type Hints:</strong></div>
      {Object.keys(data.type_hints).length > 0 ? (
        <ul>
          {Object.entries(data.type_hints).map(([key, value]) => (
            <li key={key}>{key}: {value}</li>
          ))}
        </ul>
      ) : (
        <p>No type hints available.</p>
      )}
      <div><strong>Result:</strong> {data.result}</div>
    </div>
  );
};

export default PrettyJsonDisplay;