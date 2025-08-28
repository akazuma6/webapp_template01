// frontend/src/App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Header from './components/Header';
import PostForm from './components/PostForm';

const API_URL = "http://127.0.0.1:8000/api/posts/";

function App() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    axios.get(API_URL)
      .then(res => {
        setPosts(res.data);
      })
      .catch(error => {
        console.error("There was an error fetching the posts!", error);
      });
  }, []); // 第2引数の[]は「最初の一回だけ実行する」という意味

  return (
    <div className="App">
      <Header />
      <PostForm />
      <main className="App-main">
        {posts.map(post => (
          <article key={post.id} className="post-excerpt">
            <h2>{post.title}</h2>
            <p>{post.content.substring(0, 100)}...</p>
            <small>Posted on: {post.created_at}</small>
          </article>

        ))}
      </main>
    </div>
  );
}

export default App;