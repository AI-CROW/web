package com.crow.crow.article;


import com.fasterxml.jackson.annotation.JsonProperty;

import java.util.UUID;

public class Article {
    private final UUID id;
    private final String title;
    private final String postDate;
    private String content;
    private final String url;
    private final UUID site_id;
    private final UUID author_id;

    public Article(@JsonProperty("id") UUID id,
                   @JsonProperty("title") String title,
                   @JsonProperty("postDate") String postDate,
                   @JsonProperty("content") String content,
                   @JsonProperty("url") String url,
                   @JsonProperty("site_id") UUID site_id,
                   @JsonProperty("author_id") UUID author_id ) {
        this.id = id;
        this.title = title;
        this.postDate = postDate;
        this.content = content;
        this.url = url;
        this.site_id = site_id;
        this.author_id = author_id;
    }

    public UUID getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public String getPostDate() {
        return postDate;
    }

    public String getContent() {
        return content;
    }

    public String getUrl() {
        return url;
    }

    public UUID getSite_id() {
        return site_id;
    }

    public UUID getAuthor_id() {
        return author_id;
    }

    public void setContent(String content) {
        this.content = content;
    }
}
