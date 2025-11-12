from django.db import models


class Roast(models.Model):
    """Model to store resume roasts"""
    resume_text = models.TextField(help_text="The original resume text")
    roast_text = models.TextField(help_text="The AI-generated roast")
    timestamp = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0, help_text="Number of upvotes")
    
    class Meta:
        ordering = ['-timestamp']
        
    def __str__(self):
        return f"Roast from {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

